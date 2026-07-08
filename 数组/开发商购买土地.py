def main():
    import sys 
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    
    # sum是所有土地的价值总和
    sum = 0
    # vec是土地价值矩阵
    vec = []
    for i in range(n):
        row = []
        for j in range(m):
            num = int(data[index])
            index += 1
            row.append(num)
            sum += num
        vec.append(row)
    
    # 统计各行之和
    horizontal = [0] * n
    for i in range(n):
        for j in range(m):
            horizontal[i] += vec[i][j]
    # 统计各列之和
    vertical = [0] * m
    for j in range(m):
        for i in range(n):
            vertical[j] += vec[i][j]
            
    result = float('inf')
    # 横着切找差值最小
    horizontalCut = 0
    for i in range(n):
        horizontalCut += horizontal[i]
        result = min(result,abs(sum-2*horizontalCut))
    # 竖着切找差值最小
    verticalCut = 0
    for i in range(m):
        verticalCut += vertical[i]
        result = min(result,abs(sum-2*verticalCut))
    
    print(result)
    
if __name__ == "__main__":
    main()
    