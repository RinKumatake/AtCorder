# https://atcoder.jp/contests/abc091/tasks/abc091_b
import collections
n = int(input())
blue = [input() for i in range(n)]
blue_count = collections.Counter(blue)
m = int(input())
red = [input() for i in range(m)]
red_count = collections.Counter(red)
yen = []
for k, v in blue_count.items():
    if k in red_count:
        x = red_count[k]
        count = v - x
        yen.append(count)
    else:
        yen.append(v)
y = max(yen)
print(max(0, y))

