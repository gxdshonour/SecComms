def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    
    
    
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)
    
    
def find_uv(p, q):
    gcd, u, v = extended_gcd(p, q)
    return u



# using p and q as our ptimes
p = 26513
q = 32321

# Find u
u = find_uv(p, q)


print(f"The value of u is: {u}")
