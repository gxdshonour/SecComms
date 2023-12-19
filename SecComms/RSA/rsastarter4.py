# i imported sympy to help 
# with the calculation

from sympy import mod_inverse 
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
N = p * q

# getting the totient
totient = (p - 1) * (q - 1)
# Find modular multiplicative inverse of e mod n totient will be
d = mod_inverse(e, totient)

print(d)
