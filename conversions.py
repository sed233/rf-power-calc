import math

def mw_to_dbm(power_mw):
    """Convert power in milliwatts to dBm."""
    if isinstance(power_mw, bool) or not isinstance(power_mw, (int, float)):
        raise TypeError("Power must be a number.")

    if power_mw == 0:
        return float("-inf")
    if power_mw < 0:
        raise ValueError("Power must be greater than 0 mW.")

    return round(10 * math.log10(power_mw), 4)