N,Y = map(int, input().split())

for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            if (i+j+k == N) and (10000*i + 5000*j + 1000*k == Y):
                print("{} {} {}".format(i,j,k))
                exit()

print("-1 -1 -1")

# 感想：処理時間が制限時間を超過したのでNG。ついにアルゴリズムを考えないといけないところに来たようですね。。。
# お手本見てちょっとした工夫でどうにかなったことに気づかされた。反省。。。