#!/usr/bin/env python3
"""
Build script for easy-mcp-server.
Usage:
  python scripts/build.py [command]

Commands:
  clean        - Remove build artifacts
  build        - Build distribution packages
  publish      - Publish to PyPI
  publish-test - Publish to TestPyPI
  test         - Run tests
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

# Get the project root directory
ROOT = Path(__file__).parent.parent.absolute()

def clean():
    """Remove build artifacts."""
    print("Cleaning build artifacts...")
    paths = [
        ROOT / "build",
        ROOT / "dist",
        *list(ROOT.glob("*.egg-info")),
        *list(ROOT.glob("**/__pycache__")),
    ]
    
    for path in paths:
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    
    print("Done cleaning.")

def build():
    """Build distribution packages."""
    print("Building distribution packages...")
    clean()
    subprocess.run(
        [sys.executable, "-m", "build"],
        cwd=ROOT,
        check=True,
    )
    print("Build completed.")

def publish(test=False):
    """Publish packages to PyPI or TestPyPI."""
    repository = "--repository" if test else ""
    repo_name = "testpypi" if test else ""
    target = "TestPyPI" if test else "PyPI"
    
    print(f"Publishing to {target}...")
    build()
    
    cmd = [sys.executable, "-m", "twine", "upload"]
    if test:
        cmd.extend([repository, repo_name])
    cmd.append("dist/*")
    
    subprocess.run(cmd, cwd=ROOT, check=True)
    print(f"Published to {target}.")

def run_tests():
    """Run tests."""
    print("Running tests...")
    subprocess.run(
        [sys.executable, "-m", "pytest"],
        cwd=ROOT,
        check=True,
    )
    print("Tests completed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
        
    command = sys.argv[1]
    
    if command == "clean":
        clean()
    elif command == "build":
        build()
    elif command == "publish":
        publish()
    elif command == "publish-test":
        publish(test=True)
    elif command == "test":
        run_tests()
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1) 