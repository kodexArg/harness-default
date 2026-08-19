#!/usr/bin/env python3
"""Runner for all harness self-tests."""

import sys
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent

def main() -> int:
    tests = [
        HERE / "test_adr_schema.py",
        HERE / "test_agent_definition_contract.py",
        HERE / "test_hooks_execution.py",
        HERE / "test_vault_graph.py",
    ]

    failed = 0
    for t in tests:
        print(f"Running {t.name}...")
        res = subprocess.run([sys.executable, str(t)])
        if res.returncode != 0:
            failed += 1
    if failed:
        print(f"\n❌ {failed} test suite(s) failed.")
        return 1
    print("\n✅ All harness tests passed successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
