import numpy as np

vector1 = np.array((6, 2, -3))


vector2 = np.array((5, 1, 4))


vector3 = np.array((2, 7, 1))

A = np.array((vector1, vector2, vector3))


area = np.abs(np.linalg.det(A))


result = round(area)
print(result)
