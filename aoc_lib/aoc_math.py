def euclide(a, b):
    if b == 0: return a
    return euclide(b, a % b)