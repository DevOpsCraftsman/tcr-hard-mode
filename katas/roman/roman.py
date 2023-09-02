def roman(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return ""
    return "I" * n
