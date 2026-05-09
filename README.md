# rf-power-calc

A Python utility for converting RF power milliWatts to dBm measurements.

## Background

RF engineers commonly have to convert power in milliWatts to dBm using the logarithmic function dBm = 10 * log10(power_mw / 1 mW) for signal measurements.

## Install

Requires Python 3.10 or later.

```bash
git clone https://github.com/sed233/rf-power-calc.git
cd rf-power-calc
```

## Usage

From the project folder, open Python:

```bash
python3
```

Import the function and use it:

```python
>>> from conversions import mw_to_dbm
>>> mw_to_dbm(1.0)
0.0
>>> mw_to_dbm(10)
10.0
```

Bad inputs raise errors:

```python
>>> mw_to_dbm(0)         # ValueError
>>> mw_to_dbm("hello")   # TypeError
>>> mw_to_dbm(True)      # TypeError - bools are rejected on purpose
```

Booleans are rejected explicitly because Python counts `True` as `1` and `False` as `0`, which would let `mw_to_dbm(True)` silently return `0.0`.

## API

`mw_to_dbm(power_mw)` — returns the dBm equivalent of a power value in milliwatts.

- Input: int or float, must be positive
- Output: float, rounded to 4 decimals
- Raises `TypeError` if input is not a number (or is a bool)
- Raises `ValueError` if input is zero or negative

Formula: `dBm = 10 * log10(P_mW / 1 mW)`

## Contributing

This is a coursework project for Cornell SYSEN 5493. Not accepting outside contributions right now, but feel free to open an issue if something's broken.

## License

All rights reserved. This is coursework for Cornell SYSEN 5493 (Spring 2026).