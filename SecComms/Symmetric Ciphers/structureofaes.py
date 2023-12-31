def matrix2bytes(matrix):
    return [x for l in matrix for x in l]

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]


bytes(matrix2bytes(matrix))