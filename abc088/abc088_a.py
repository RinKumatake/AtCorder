# https://atcoder.jp/contests/abc088/tasks/abc088_a
n = int(input())
a = int(input())
x = n % 500
if x <= a:
    print("Yes")
else:
    print("No")