a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
# print('a:b:c:x={}:{}:{}:{}'.format(a,b,c,x))

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if (500*i+100*j+50*k == x): # 考え方的には総当たりで計算するってやり方
                ans += 1

print(ans)