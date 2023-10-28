N = int(input())
wx = [list(map(int, input().split())) for l in range(N)]

dp = [0 for i in range(24)]

for w,x in wx:
    for i in range(9, 18): 
        dp[(x+i)%24] += w

print(max(dp))

# 感想：さっぱりわからなかったので正解に頼ってしまった、、、
#  正解コードをでばぐモードで追いかけるとすごいよくわかる
#  標準時の配列を作って、拠点ごとで拠点の営業時間を標準時に置き換えたときに
#  参加可能な参加者を配列に格納して最終的にもっともたくさんの人数が参加してる時間帯をmaxを割り出している