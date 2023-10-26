N = int(input())
#空のリスト
A = []
#リストAにappend()を使って格納していく
for _ in range(N):
    A.append(int(input()))

u_arr = list(set(A))
ans = len(u_arr)

print(ans)
# 感想：pythonに便利な関数あるので使い方を調べるだけで回答できた