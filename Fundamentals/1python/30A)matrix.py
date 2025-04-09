def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication'nt possible.")
        return None
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

matrix1 = [[1, 2, 3],
           [44, 55, 66],
           [0, 64, 9]]

matrix2 = [[9, 0, 7],
           [61, 52, 47],
           [3, 2, 0]]

result_matrix = matrix_multiply(matrix1, matrix2)

if result_matrix:
    for row in result_matrix:
        print(row)
