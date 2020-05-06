# https://atcoder.jp/contests/abc092/tasks/abc092_b
n = int(input())
d, x = map(int, input().split())
counts = x
for i in range(n):
    a = int(input())
    count = 1 + (d-1)//a
    counts += count
print(counts)

        
