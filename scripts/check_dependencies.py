#!/usr/bin/env python3

import re
import subprocess
import sys
from typing import List, NoReturn, Optional, Tuple

python_version: Tuple[int, int] = (3, 9)
cmake_version: Tuple[int, int] = (3, 14)
arduino_cli_version: Tuple[int, int] = (0, 19)

python_version_pattern: re.Pattern = re.compile(
    r"Python (?P<version>[1-9]\.[0-9]+)"
)
cmake_version_pattern: re.Pattern = re.compile(
    r"cmake version (?P<version>[1-9]\.[0-9]+)"
)
arduino_cli_version_pattern: re.Pattern = re.compile(
    r"Version: (?P<version>[0-9]\.[0-9]+)"
)


def error(message: str) -> NoReturn:
    """Print an error message to the user and exit script with error.

    Args:
        message: Error message to be printed"""
    print(message)
    sys.exit(1)


def check_program(args: List[str]) -> Tuple[int, Optional[str]]:
    """Execute a program on the command line and check its result.

    Args:
        args: List of string arguments to run on the command line.

    Returns:
        Tuple of return code and output as string (if any).
    """
    try:
        completed_process = subprocess.run(args, capture_output=True)
        output: Optional[str] = None

        if (
            len(completed_process.stdout) > 0
            or len(completed_process.stderr) > 0
        ):
            output = str(completed_process.stdout) + str(
                completed_process.stderr
            )

        return (completed_process.returncode, output)

    except Exception:
        return (-1, None)


def check_version(available: str, needed: Tuple[int, int]) -> bool:
    """Check that an available version matches the needed version."""
    major, minor = available.split(".")
    if int(major) < needed[0]:
        return False
    return int(minor) >= needed[1]


def check_arduino_cli() -> None:
    """Check that arduino-cli is available"""
    retcode, output = check_program(["arduino-cli", "version"])

    if retcode != 0 or output is None:
        error("Could not find `arduino-cli` executable")

    match = arduino_cli_version_pattern.search(output)
    if match is None:
        error("Could not determine arduino-cli version")
    version: str = match["version"]

    if not check_version(version, arduino_cli_version):
        error("arduino-cli version is outdated, please install version >=0.19")


def check_black() -> None:
    """Check that Black is available"""
    retcode, _ = check_program(["black", "--version"])

    if retcode != 0:
        error("Could not find `black` executable")


def check_pyre() -> None:
    """Check that Pyre is available"""
    retcode, _ = check_program(["pyre", "--version"])

    if retcode != 0:
        error("Could not find `pyre` executable")


def check_cmake() -> None:
    """Check that CMake is available"""
    retcode, output = check_program(["cmake", "--version"])

    if retcode != 0 or output is None:
        error("Could not find `cmake` executable")

    match = cmake_version_pattern.search(output)
    if match is None:
        error("Could not determine cmake version")
    version: str = match["version"]

    if not check_version(version, cmake_version):
        error("CMake version is outdated, please install version >=3.14")


def check_python() -> None:
    """Check if the python version is >= 3.9"""
    retcode, output = check_program(["python3", "--version"])

    if retcode != 0 or output is None:
        error("Could not find `python3` executable")

    match = python_version_pattern.search(output)
    if match is None:
        error("Could not determine python version")
    version: str = match["version"]

    if not check_version(version, python_version):
        error("Python version is outdatedm Please install version >=3.9")


def main() -> None:
    """Check binary dependencies."""
    check_python()
    check_cmake()
    check_arduino_cli()
    check_pyre()
    check_black()

    print("All binary dependencies OK!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        error(str(e))
