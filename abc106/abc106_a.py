# https://atcoder.jp/contests/abc106/tasks/abc106_a

a, b = map(int, input().split())
road = (1*b + 1*a)-1
print(a * b - road)