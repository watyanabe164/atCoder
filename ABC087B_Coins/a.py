a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
#print('a:b:c:x={}:{}:{}:{}'.format(a,b,c,x))

# 3回forを回す作戦
# 500円玉があるだけ回す
for i in range(a+1):
    p = x -500*i
    for j in range(b+1):
        q = p - 100*j
        for k in range(c+1):
            if (q > 0) and (q - 50*k == 0):
                ans += 1

print(ans)

# 感想：3回forを回すところはよかったけど15行目のところで素直にチェックすればよかったのに微妙に複雑にしてしまったために間違えた
#        お手本にa_seikai.pyを残す