n = int(input())
x = list(map(int, input().split()))
ans = []
for i in range(100):
    power = 0
    for j in x:
        power = power + ((j-i)**2)
    ans.append(power)
print(min(ans))


