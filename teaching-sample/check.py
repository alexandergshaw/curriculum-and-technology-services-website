"""Run the same behavioral checks against the reference or student workspace."""

import argparse
import os
from pathlib import Path
import sys
import unittest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("implementation", choices=["reference", "starter"], nargs="?", default="reference")
    args = parser.parse_args()
    os.environ["LAB_IMPLEMENTATION"] = args.implementation
    suite = unittest.defaultTestLoader.discover(str(Path(__file__).parent / "tests"))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
