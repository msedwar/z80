#!/usr/bin/env python3

import os
from pathlib import Path
import subprocess
import sys
from typing import Callable, Dict, List

project_path: Path = Path(__file__).parent.parent.resolve()
black_config_file: Path = Path("pyproject.toml")


def invoke_binary(args: List[str]) -> bool:
    """Invoke a linting binary.

    Args:
        args: Arguments to run command line program.

    Returns:
        True if linter successfully exited.
    """
    completed_process = subprocess.run(args, capture_output=True)
    return completed_process.returncode == 0


def lint_python(file_path: Path) -> bool:
    """Lint a Python file."""
    return invoke_binary(
        [
            "black",
            "--config",
            str(project_path / black_config_file),
            str(file_path),
        ]
    )


lint_map: Dict[str, Callable[[Path], bool]] = {
    "py": lint_python,
}


def lint_file(file_path: Path) -> bool:
    """Lint file at given path.

    Args:
        file_path: Path to file to lint.

    Returns:
        True if path successfully linted.
    """
    ext: str = file_path.suffix[1:]
    return lint_map[ext](file_path)


def file_is_lintable(file_path: Path) -> bool:
    """Check if the given file is lintable.

    Args:
        file_path: Path of file to check.

    Returns:
        True if file is lintable.
    """
    ext: str = file_path.suffix
    if len(ext) > 1:
        return ext[1:] in lint_map

    return False


def apply_to_files(
    directory: Path, pred: Callable[[Path], bool], func: Callable[[Path], bool]
) -> bool:
    """Apply a function to all files in a path (recursive) if they match the
    given predicate.

    Args:
        directory: Directory to traverse recursively.
        pred: Predicate function to match files.
        func: Function to apply to files matching predicate.
    """
    success: bool = True
    for root, _, files in os.walk(directory):
        root_path: Path = Path(root)
        for file in files:
            file_path = root_path / Path(file)
            if pred(file_path):
                success = success and func(file_path)
    return success


def lint_all() -> None:
    """Lint all files in project."""
    success: bool = apply_to_files(project_path, file_is_lintable, lint_file)

    if not success:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    lint_all()
