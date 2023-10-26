import itertools
S = input()
arr = ["erase", "eraser", "dream", "dreamer"]

for perm in itertools.permutations(arr): # ４つの文字パターンのすべての組み合わせを総当たりで確認する
    X = S
    for i in range(4):
        X = X.replace(perm[i], "")
    if X == "":
        print("YES")
        exit()

print("NO")

# 感想：正解はとれたけど、総当たりなのであまり効率が良いとはいいがたい
# ほかの人の解答を見て、いいやつ見つかったのでa_seikai.pyにおいとく