import numpy as np
#to help num operations

def gram_schmidt(basis):
    
    basis = np.array(basis, dtype=float)
    
    
    
    orthogonal_basis = np.zeros_like(basis)

    for i in range(basis.shape[0]):
        
        #if this doesnt work, re-read gram-schmmidt.
        # this seems hard honestly. reminder.
        
        # involves constructing
        # orthonormal basis with
        # set of vectors 
        
        orthogonal_basis[i] = basis[i] - sum(
            (np.dot(basis[i], orthogonal_basis[j]) / np.dot(orthogonal_basis[j], orthogonal_basis[j])) * orthogonal_basis[j]
            for j in range(i)
        )

    return orthogonal_basis

# given set of vectors
vector1 = np.array([4, 1, 3, -1], dtype=float)
vector2 = np.array([2, 1, -3, 4], dtype=float)
vector3 = np.array([1, 0, -2, 7], dtype=float)
vector4 = np.array([6, 2, 9, -5], dtype=float)

# making the basis matrix
basis_matrix = np.array([vector1, vector2, vector3, vector4])

# now use gramschmidt algorithm
orthogonal_basis = gram_schmidt(basis_matrix)







print("Orthogonal Basis")
for i, vector in enumerate(orthogonal_basis):
    print(f"u{i+1} = {vector}")

# Extract the second component of u4 to 5 significant figures
flag = round(orthogonal_basis[3, 1], 5)
print("\nFlag:", flag)
