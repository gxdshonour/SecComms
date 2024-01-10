def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)

def mod_inverse(a, m):
    d, x, y = extended_gcd(a, m)
    if d != 1:
        raise ValueError("Inverse does not exist")
    else:
        return x % m


p = 991
g = 209


inverse = mod_inverse(g, p)

print(f"Inverse is {inverse}")
