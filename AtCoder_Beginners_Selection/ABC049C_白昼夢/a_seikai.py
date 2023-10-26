import re

s = input()

pattern = "^(dream|dreamer|erase|eraser)+$"

result = re.match(pattern, s)

if result:
    print("YES")
else:
    print("NO")

# 感想：問題の理解と、正規表現をうまく使ってスマートに回答している。お手本にしよう