# https://atcoder.jp/contests/abc110/tasks/abc110_a

x = list(map(int, input().split()))
sort_x = sorted(x)
# 一番大きな数を10の位にする
print(sort_x[2]*10 + sort_x[1] + sort_x[0])

