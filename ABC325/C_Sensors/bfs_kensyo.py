# https://qiita.com/drken/items/996d80bcae64649a6580　より引用のBFS（幅優先探索）のコード
'''
入力例：
9 13
0 1
0 4
0 2
1 4
1 3
1 8
2 5
3 8
4 8
5 8
5 6
3 7
6 7
出力例：
1: 1
2: 1
3: 2
4: 1
5: 2
6: 3
7: 3
8: 2
'''

from collections import deque

# 頂点数と辺数
N, M = map(int, input().split())

# グラフ入力受取 (ここでは無向グラフを想定)
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# BFS のためのデータ構造
dist = [-1] * N # 全頂点を「未訪問」に初期化
que = deque()

# 初期条件 (頂点 0 を初期ノードとする)
dist[0] = 0
que.append(0) # 0 を橙色頂点にする

# BFS 開始 (キューが空になるまで探索を行う)
while que:
    v = que.popleft() # キューから先頭頂点を取り出す

    # v から辿れる頂点をすべて調べる
    for nv in G[v]:
        if dist[nv] != -1: continue # すでに発見済みの頂点は探索しない

        # 新たな白色頂点 nv について距離情報を更新してキューに追加する
        dist[nv] = dist[v] + 1
        que.append(nv)

# 結果出力 (各頂点の頂点 0 からの距離を見る)
for v in range(N):
    print(v, ":", dist[v])