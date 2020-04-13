n = int(input())
num = [i for i in range(1, n+1) if i%3 and i%5]
print(sum(num))

