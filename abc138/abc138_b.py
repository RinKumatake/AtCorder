n = int(input())
a = list(map(int, input().split()))
num = [1/i for i in a]
ans = 1/(sum(num))
print(ans)