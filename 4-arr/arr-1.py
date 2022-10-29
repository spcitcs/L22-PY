# Set, # Map

# satyo = [1,2,3]
# satyo.insert(0,-3)
# satyo.insert(1,-2)
# satyo.insert(2,-1)
# satyo.insert(3,0)
# print(satyo, len(satyo))

# myList = [1,2,3]
# myList.insert(0,0)
# myList.insert(0,-1)
# myList.insert(0,-2)
# myList.insert(0,-3)
# print(myList, len(myList))

# myList = [1,2,3]
# hasil = [-3,-2,-1,0] + myList

# hasil.pop()
# hasil.pop(0)

# # [-2,-1,0,1,2] 

# hasil.insert(-3,[1,2])

# print(hasil, len(hasil))

# # [-2,-1,[1,2],0,1,2]
# print(hasil[2][1]) # 

# Try and Error

matrix = [[1,2,3], # --> t -->  [[1,4,7],
          [4,5,6], #             [2,5,8],
          [7,8,9]] #             [3,6,9]]

# transpose
# expected result
# [[1,4,7],[2,5,8],[3,6,9]]

# matrixHasil = []
# matrix1 = []
# matrix1.append(matrix[0][0])
# matrix1.append(matrix[1][0])
# matrix1.append(matrix[2][0])
# matrixHasil.append(matrix1)
# matrix2 = []
# matrix2.append(matrix[0][1])
# matrix2.append(matrix[1][1])
# matrix2.append(matrix[2][1])
# matrixHasil.append(matrix2)
# matrix3 = []
# matrix3.append(matrix[0][2])
# matrix3.append(matrix[1][2])
# matrix3.append(matrix[2][2])
# matrixHasil.append(matrix3)

# matrixHasil = [
#    [matrix[0][0],matrix[1][0],matrix[2][0]],
#    [matrix[0][1],matrix[1][1],matrix[2][1]],
#    [matrix[0][2],matrix[1][2],matrix[2][2]],
# ]

# print(matrixHasil)

_A = [[1,2], # A = [[a,b],
     [3,4]] #      [c,d]]
_A = [[6,3],
     [2,7]]
A = [[5,-2],[8,6]]
det = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

print(det) # hasil determinan matrix
# -2





