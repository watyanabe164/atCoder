N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
    #上から順番に代入していく
    t[i], x[i], y[i] = map(int, input().split())

x_sabun = 0
y_sabun = 0
t_sabun = 0

for i in range(N):
    x_sabun = abs(x[i]-x_sabun)
    y_sabun = abs(y[i]-y_sabun)
    t_sabun = abs(t[i]-t_sabun)

    amari = t_sabun - (x_sabun + y_sabun)

    if amari < 0 or amari%2 != 0:
        print("No")
        exit()

print("Yes")

# 感想：お手本見て正解でた。途中でたどり着けないルートが出た場合（amari < 0 or amari%2 != 0）はそこで終了、という考えを入れてるのがポイント