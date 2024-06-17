from typing import List
def sprialOrder(matrix:List[List[int]]):
    if not matrix:
        return
    row, col = len(matrix), len(matrix[0])
    top, bottom, left, right = 0,row-1, 0,col-1
    result = []

    while len(result) < row*col:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top += 1
    
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top-1,-1):
                result.append(matrix[i][left])
            left += 1
    return result

def main():
    m = [[1,2,3],[4,5,6],[7,8,9]]
    res = sprialOrder(m)
    print(res)

main()