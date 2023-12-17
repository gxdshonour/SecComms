def gcd(a, b):
    
    while b:
        
        a, b = b, a % b
    return a


case_a = 12
case_b = 8
result = gcd(test_a, test_b)
print(f"GCD of {case_a} and {case_b} will be: {result}")
