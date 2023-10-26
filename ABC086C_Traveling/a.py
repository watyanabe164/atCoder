N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
    #上から順番に代入していく
    t[i], x[i], y[i] = map(int, input().split())