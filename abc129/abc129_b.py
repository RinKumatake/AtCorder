# https://atcoder.jp/contests/abc129/tasks/abc129_b

n = int(input())
w = list(map(int, input().split()))
difference = []
for i in range(n):
    s1 = w[0:i+1]
    s2 = w[i+1:n]
    s = abs(sum(s1)-sum(s2))
    difference.append(s)
print(min(difference))