def find_primitive_element(p):
    for g in range(2, p):
        is_primitive = True
        for k in range(1, p-1):
            if pow(g, k, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return g

# Given value
p = 28151

primitive_element = find_primitive_element(p)

print(f"Smallest primitive element is {primitive_element}")
