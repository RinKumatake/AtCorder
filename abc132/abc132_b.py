# https://atcoder.jp/contests/abc132/tasks/abc132_b
n  = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(1,n-1):
    p_1 = p[i-1]
    p_2 = p[i]
    p_3 = p[i+1]
    if p_1 < p_2 < p_3 or p_1 > p_2 > p_3:
        count += 1
print(count)



