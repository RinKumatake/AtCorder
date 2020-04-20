s = input()
num = []
for i in range(len(s)-2):
    x = int(s[i:i+3])
    n = abs(753 - x)
    num.append(n)
print(min(num))