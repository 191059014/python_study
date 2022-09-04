while True:
    try:
        x = int(input())
        y = int(input())
        z = int(input())
        A, B = [], []
        res = [[0] * z for _ in range(x)]
        for i in range(x):
            A.append(list(map(int, input().split())))
        for j in range(y):
            B.append(list(map(int, input().split())))
        for i in range(x):
            for j in range(z):
                for k in range(y):
                    res[i][j] += A[i][k] * B[k][j]
        for line in res:
            print(*line)
    except:
        break