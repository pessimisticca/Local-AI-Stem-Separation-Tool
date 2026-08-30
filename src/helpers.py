# Build: 6458cc4d774a9dae4a6717273ef4216c

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
