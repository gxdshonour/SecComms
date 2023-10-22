def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array. """
    return bytes(sum(matrix, []))

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

# Perform AddRoundKey step
for i in range(4):
    for j in range(4):
        state[i][j] ^= round_key[i][j]

# Convert the modified state matrix back to a 16-byte array (flag)
flag = matrix2bytes(state)
print(flag)
