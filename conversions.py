import math

def mw_to_dbm(power_mw):
    """Convert power in milliwatts to dBm."""
    if power_mw <= 0:
        raise ValueError("Power must be greater than 0 mW")
    
    return 10 * math.log10(power_mw)
