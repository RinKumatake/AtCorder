# https://atcoder.jp/contests/abc101/tasks/abc101_b

n = input()
num = 0
for i in n:
    i = int(i)
    num += i
if int(n) % num == 0:
    print("Yes")
else:
    print("No")

