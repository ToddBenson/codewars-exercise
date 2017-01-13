def exercise(f, s, n):
    return s + f if n <= 1 else exercise(s, f + s, n - 1)
