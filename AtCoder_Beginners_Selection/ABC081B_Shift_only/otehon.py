N = int(input())

A = list(map(int, input().split()))

count = 0

while all(a % 2 == 0 for a in A): 
## all()とforを組み合わせることでAに入ってるすべての要素が2で割り切れるかどうか判定

    A = [a // 2 for a in A]
    ## a // 2ってやることで整数で割り算（小数点以下切捨て）になる
    count += 1 ## pythonではインクリメントはこうやる

print(count)