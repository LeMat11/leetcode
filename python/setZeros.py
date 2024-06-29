from typing import List

def setZeros(matrix:List[List[int]]):
    m = len(matrix)
    n = len(matrix[0])
    zeros = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros.append((i,j))
    for zero in zeros:
        i = zero[0]
        j = zero[1]
        matrix[i] = [0 for num in matrix[i]]
        for k in range(m):
            matrix[k][j] = 0
    return matrix

matrix = [
    [0, 2, 0],
    [4, 5, 6],
    [7, 8, 9]
]
res= setZeros(matrix)
print(res)
