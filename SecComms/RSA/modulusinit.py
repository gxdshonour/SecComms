from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

e = 65537  # Use a common and recommended value for e
d = -1

while d == -1:
    p = getPrime(1024)
    q = getPrime(1024)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)

n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

# Include the calculation of d
pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
assert decrypted == flag

print("Decrypted Flag:", decrypted.decode())
