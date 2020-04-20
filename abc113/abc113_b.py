# https://atcoder.jp/contests/abc113/tasks/abc113_b
n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
palace = []
for i in range(1, n+1):
    candidate =[]
    temperature =abs(a -(t - h[i-1] *0.006))
    candidate.append(temperature)
    candidate.append(i)
    palace.append(candidate)
sort_palace = sorted(palace)
print(sort_palace[0][1])
    

    

