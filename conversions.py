import math


def mw_to_dbm(power_mw):
    """Convert power in milliwatts to dBm."""
    if isinstance(power_mw, bool) or not isinstance(power_mw, (int, float)):
        raise TypeError("Power must be a number.")

    if power_mw <= 0:
        raise ValueError(f"Power must be > 0 mW; got {power_mw} mW (log10 undefined for non-positive)")

    return round(10 * math.log10(power_mw), 4)
