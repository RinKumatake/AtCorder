# https://atcoder.jp/contests/abc137/tasks/abc137_b
k, x = map(int, input().split())
a = k - 1
b = [str(i) for i in range(x-a, x+a+1)]
print(" ".join(b))
