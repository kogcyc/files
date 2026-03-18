#!/usr/bin/env python3

import argparse
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

# Update this to the directory that hosts the target scripts.
BASE_URL = "https://kogcyc.github.io/files/remote"

SCRIPT_NAME_RE = re.compile(r"^[A-Za-z0-9_-]+$")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download a Python script from a base URL and execute it."
    )
    parser.add_argument(
        "script_name",
        help="Script name without the .py suffix, for example: name",
    )
    parser.add_argument(
        "script_args",
        nargs=argparse.REMAINDER,
        help="Arguments passed through to the downloaded script.",
    )
    parser.add_argument(
        "--base-url",
        default=BASE_URL,
        help="Override the default base URL.",
    )
    return parser


def validate_script_name(script_name: str) -> None:
    if not SCRIPT_NAME_RE.fullmatch(script_name):
        raise ValueError(
            "script_name must contain only letters, numbers, underscores, or hyphens"
        )


def download_script(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "python-bootstrap-runner/1.0"},
    )
    with urllib.request.urlopen(request) as response:
        return response.read()


def main() -> int:
    args = build_parser().parse_args()

    try:
        validate_script_name(args.script_name)
    except ValueError as exc:
        print(f"Invalid script name: {exc}", file=sys.stderr)
        return 2

    base_url = args.base_url.rstrip("/")
    url = f"{base_url}/{args.script_name}.py"

    try:
        script_bytes = download_script(url)
    except urllib.error.HTTPError as exc:
        print(f"Download failed: {exc.code} {exc.reason} for {url}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"Download failed: {exc.reason} for {url}", file=sys.stderr)
        return 1

    with tempfile.NamedTemporaryFile(
        mode="wb",
        suffix=".py",
        prefix=f"{args.script_name}_",
        delete=False,
    ) as temp_file:
        temp_file.write(script_bytes)
        temp_path = temp_file.name

    try:
        completed = subprocess.run(
            [sys.executable, temp_path, *args.script_args],
            check=False,
        )
        return completed.returncode
    finally:
        try:
            os.unlink(temp_path)
        except OSError:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
