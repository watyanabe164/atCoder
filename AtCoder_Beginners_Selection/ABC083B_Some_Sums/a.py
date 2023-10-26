n,a,b = map(int, input().split())

# print('n:a:b={}:{}:{}'.format(n,a,b))
ans = 0

for i in range(n+1):
    l = [int(j) for j in str(i)]
    if a <= sum(l) <= b:
#        print(i)
        ans += i

print(ans)
# 感想：python的書き方（7,8行目）でちょっと調べたけど、やりたいことは愚直な計算だったので比較的楽でした