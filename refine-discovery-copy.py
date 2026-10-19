"""Deprecated historical generator: rebuild current reviewed source without overwriting it."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    print("Deprecated command: using package.py; reviewed documents and test results are preserved.")
    runpy.run_path(str(Path(__file__).with_name("package.py")), run_name="__main__")
