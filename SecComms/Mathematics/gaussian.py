# Read up gaussian lattice to understand more.
# honour, please dont forget.

import math

# first find the dot product of two vextors
def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def gaussian_lattice_reduction(vector1, vector2):
    
    
    
    # if my vector2 less than vector1 swap dem 
    
    if dot_product(vector2, vector2) < dot_product(vector1, vector1):
        vector1, vector2 = vector2, vector1
    
    while True:
        # Compute m = floor(vector1 · vector2 / ||vector1||^2)
        m = math.floor(dot_product(vector1, vector2) / dot_product(vector1, vector1))
        
        # now to return vector1, vector2 if m gives 0, 
        if m == 0:
            return vector1, vector2
        
        
        
        # took a break. headache. come back to work.
        
       
        vector2 = [vector2[i] - m * vector1[i] for i in range(len(vector1))]

# using the given vectors
v = [846835985, 9834798552]

u = [87502093, 123094980]

#  gaussian lattice reduction


vector1, vector2 = gaussian_lattice_reduction(v, u)




# Calculate the inner product of the new basis vectors
flag = dot_product(vector1, vector2)


print("vector1", vector1)


print("vector2", vector2)



print("flag", flag)
