def transpose(matrix):
    row=len(matrix)
    col=len(matrix[0])
    tran=[[0 for p in range(row)]for p in range(col)]
    for i in range (row):
        for j in range (col):
            tran[i][j]=matrix[j][i]
    return tran

matrix=[[5,9,4],[7,0,4],[8,0,6]]
print(transpose(matrix))