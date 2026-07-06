n = int(input())
def generateMatrix(n):
    matrix = [[0]*n for _ in range(n)]
    startx,starty = 0,0      # 起始点
    loop,mid = n//2,n//2     # 迭代次数、n为奇数时，矩阵的中心点
    count = 1                # 计数
    
    for offset in range(1,loop+1):
        for i in range(starty, n-offset):  # 上行从左到右
            matrix[startx][i] = count
            count += 1
        for i in range(startx, n-offset):  # 右列从上到下
            matrix[i][n-offset] = count
            count += 1 
        for i in range(n-offset, starty, -1):  # 下行从右到左
            matrix[n-offset][i] = count
            count += 1
        for i in range(n-offset, startx, -1):  # 左列从下到上
            matrix[i][starty] = count
            count += 1
        startx += 1         # 更新起始点
        starty += 1
    if n % 2 != 0 :			# n为奇数时，填充中心点
        matrix[mid][mid] = count 
    
    return matrix
matrix = generateMatrix(n)
print(matrix)
