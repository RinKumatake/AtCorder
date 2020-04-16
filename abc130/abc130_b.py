# https://atcoder.jp/contests/abc130/tasks/abc130_b
n, x = map(int, input().split())
l = list(map(int, input().split()))
ball = 1
bound = 0
for i in l:
    bound = bound + i
    if bound > x:
        break
    ball += 1
print(ball)
    