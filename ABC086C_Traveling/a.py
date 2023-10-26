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

if (x_sabun + y_sabun) == 0 or t_sabun == 0:
    if t_sabun%2 == 0:
        print("Yes")
    else:
        print("No")
else:
    if t_sabun%abs(x_sabun + y_sabun) == 0:
        print("Yes")
    else:
        print("No")

# 感想：不正解。このやり方、ぱっと見正解のように思ってたけど、途中でたどり着けない、という考えが抜け落ちたものになってた
