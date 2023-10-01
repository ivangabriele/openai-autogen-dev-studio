def mask_secret(value: str) -> str:
    """Mask a secret value, revealing only the first 3 and last 3 characters."""
    if len(value) <= 6:
        return "*" * len(value)
    return value[:3] + "*" * (len(value) - 6) + value[-3:]
