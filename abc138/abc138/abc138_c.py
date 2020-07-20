n = int(input())
v = list(map(int, input().split()))
sort_v = sorted(v)
ans = sort_v[0]
for i in sort_v[1:]:
    ans = (ans + i)/2
print(ans)

