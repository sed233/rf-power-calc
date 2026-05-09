"""Tests for conversions.py."""

import pytest

from conversions import mw_to_dbm


# Reference values from the dBm definition:
#   1 mW   = 0 dBm
#   10 mW  = 10 dBm
#   0.1 mW = -10 dBm
def test_one_mw_is_zero_dbm():
    assert mw_to_dbm(1.0) == pytest.approx(0.0)


def test_ten_mw_is_ten_dbm():
    assert mw_to_dbm(10) == pytest.approx(10.0)


def test_point_one_mw_is_negative_ten_dbm():
    assert mw_to_dbm(0.1) == pytest.approx(-10.0)


def test_int_input_works():
    """Function should accept int as well as float."""
    assert mw_to_dbm(100) == pytest.approx(20.0)


def test_result_is_rounded_to_4_decimals():
    """Output precision should match what we documented."""
    result = mw_to_dbm(1.5)
    # Check it has at most 4 decimals by comparing to its rounded self
    assert result == round(result, 4)


# Validation tests
def test_zero_raises_value_error():
    with pytest.raises(ValueError):
        mw_to_dbm(0)


def test_negative_raises_value_error():
    with pytest.raises(ValueError):
        mw_to_dbm(-1.0)


def test_string_raises_type_error():
    with pytest.raises(TypeError):
        mw_to_dbm("ten")


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        mw_to_dbm(None)


def test_bool_raises_type_error():
    """Booleans are subclass of int in Python; we reject them explicitly."""
    with pytest.raises(TypeError):
        mw_to_dbm(True)
    with pytest.raises(TypeError):
        mw_to_dbm(False)


def test_value_error_message_includes_offending_value():
    """The merge resolution kept the f-string error; confirm it shows."""
    with pytest.raises(ValueError, match="-5"):
        mw_to_dbm(-5)
