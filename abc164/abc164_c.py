import collections
n = int(input())
p = [input() for i in range(n)]
x = collections.Counter(p)
print(len(x))
