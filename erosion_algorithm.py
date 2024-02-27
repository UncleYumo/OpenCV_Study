

def showMatrix(matrix):
    print("------------------------------")
    if matrix == None:
        print("Get None......")
        print("------------------------------")
    else:
        for row in matrix:
            print(row)
        print("------------------------------")
matrix = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

kernel = [
    [1,1],
    [1,1]
]

locate_matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

matrix_lenth=10
kernel_lenth=2
# row=0
# row_range=9
# col=0
# col_range=9
times= matrix_lenth - kernel_lenth + 1

for row in range(0, times):
    for col in range(0, times):
        evaluate = matrix[row][col] == 0 or matrix[row + 1][col] == 0 or matrix[row][col + 1] == 0 or matrix[row + 1][col + 1]==0
        if evaluate:
            locate_matrix[row][col]=0
            locate_matrix[row][col+1] = 0
            locate_matrix[row+1][col] = 0
            locate_matrix[row+1][col+1] = 0

#showMatrix(matrix)
#showMatrix(locate_matrix)