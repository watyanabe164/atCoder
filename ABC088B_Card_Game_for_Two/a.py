n = int(input())
a= list(map(int, input().split()))
alice = 0
bob = 0
while a:
    alice += max(a)
    a.remove(max(a))
    if a:
        bob += max(a)
        a.remove(max(a))
    else:
        break

print(alice-bob)
# 感想：配列の扱いについてはbing aiに聞いたけど、考え方はかなり思った通りのやり方で答えが出せたので良かった
#       ほかのお手本では、最初にソートしてその後はソートされたものの性質を使って処理する方式をとっていたけどメモリめっちゃ食うしそんなに早くないので自分のやり方のほうが気に入ってる