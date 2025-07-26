"""Custom code quality check implementation."""

import sys
import pathlib


def assert_short_filenames(filenames=None, *, min_len=3):
    filenames = sys.argv[1:] if filenames is None else filenames
    bad_ones = [
        filename for filename in filenames if len(pathlib.Path(filename).stem) < min_len
    ]
    for bo in bad_ones:
        print(f"!{min_len=}: {bo}")

    sys.exit(bool(bad_ones))
