import collections
n = int(input())
a = list(map(int, input().split()))
x = collections.Counter(a)
for i in range(1,n+1):
    print(x[i])
