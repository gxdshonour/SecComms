# let
M = 12
e = 65537
p = 17
q = 23
# solve for N
N = p * q
# encryption
ciphertext = pow(M, e, N)
print(ciphertext)
