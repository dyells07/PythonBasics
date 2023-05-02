def matrix_find(matrix,value):
    if not matrix or not matrix[0]:
        return False
    
    j = len(matrix[0])-1
    for row in matrix:
        while row[j] > value:
            j=j-1
            if j ==-1:
                return False
        if row[j] == value:
            return True
        return False
    
matrix =[[3,4,5,6],[7,8,9,10],[11,12,13,14],[15,16,17,18]]
print(matrix_find(matrix, 10))