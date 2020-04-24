# https://atcoder.jp/contests/abc152/tasks/abc152_c
n = int(input())
p = list(map(int, input().split()))
count = 1
tmp = p[0]
for i in p:
    a = min(tmp, i)
    if tmp != a:
        count+=1
        tmp = a
print(count)
    


