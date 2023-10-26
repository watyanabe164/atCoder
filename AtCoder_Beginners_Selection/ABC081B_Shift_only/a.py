N = int(input())
l = list(map(int, input().split()))
a = 0
#print(l)
while True:
    for _ in l:
        if _%2 != 0:
            print(a)
            exit()
    l = [x / 2 for x in l]
    a +=1

# 感想：配列の中の内容をすべて半分にするっていうところをリスト内包表記使ったら余裕なところに気づいたまではよかったけどやり方忘れたので調べる羽目になった
#      お手本の書き方のほうが好きなのでotehon.py残した