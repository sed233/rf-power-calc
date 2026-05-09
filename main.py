"""Command-line interface for the mw_to_dbm conversion."""

import sys

from conversions import mw_to_dbm


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <power_in_mw>")
        print("Example: python3 main.py 10")
        sys.exit(1)

    try:
        power_mw = float(sys.argv[1])
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a number.")
        sys.exit(1)

    try:
        dbm = mw_to_dbm(power_mw)
        print(f"{power_mw} mW = {dbm} dBm")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
