# https://atcoder.jp/contests/abc164/tasks/abc164_c
import collections
n = int(input())
p = [input() for i in range(n)]
x = collections.Counter(p)
print(len(x))
