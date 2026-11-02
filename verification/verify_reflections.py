#!/usr/bin/env python3
"""Run the independent finite pair/tree field checks and retain their reports."""
from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import scipy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("reflection_results.json"))
    args = parser.parse_args()
    output = args.output
    scripts = Path(__file__).resolve().parent
    optimized = ["-O"] if sys.flags.optimize else []
    children = [("pair", "check_reflection_pair.py"),
                ("tree", "check_reflection_tree.py")]
    rows = []
    with tempfile.TemporaryDirectory(prefix="reflection-checks-") as temporary:
        reports = []
        for name, script in children:
            temporary_report = Path(temporary) / f"{name}.json"
            command = [sys.executable, *optimized, str(scripts / script),
                       "--output", str(temporary_report)]
            completed = subprocess.run(command, capture_output=True, text=True)
            if completed.returncode != 0:
                sys.stderr.write(completed.stderr or completed.stdout)
                raise SystemExit(completed.returncode)
            report = json.loads(temporary_report.read_text())
            if report.get("status") != "passed":
                raise RuntimeError(f"{script} did not report a passing comparison")
            destination = output.with_name(f"{output.stem}_{name}.json")
            summary = report.get("summary")
            if summary is None:
                summary = {
                    "uniform_analytic_distance_lower_bound":
                        report["uniform_analytic_distance_lower_bound"],
                    "finite_word_cases": len(report["finite_word_checks"]),
                    "original_field_blindness_error":
                        report["maximum_original_identity_loop_field_difference"],
                    "number_dephased_field_difference":
                        report["maximum_total_number_dephased_field_difference"],
                }
            rows.append({"name": name, "program": script, "status": "passed",
                         "report": destination.name, "summary": summary})
            reports.append((temporary_report, destination))
        output.parent.mkdir(parents=True, exist_ok=True)
        for source, destination in reports:
            shutil.copyfile(source, destination)
        result = {"status": "passed", "python": platform.python_version(),
                  "numpy": np.__version__, "scipy": scipy.__version__,
                  "checks_active_under_optimization": True,
                  "checks": rows,
                  "scope": "Finite diagnostics supplement the analytical proofs; "
                           "this is not an asymptotic, priority, or hosted-rendering certificate."}
        output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
