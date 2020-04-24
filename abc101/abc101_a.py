# https://atcoder.jp/contests/abc101/tasks/abc101_a
a = input()
b = 0
for i in a:
    if i =="+":
        b += 1
    else:
        b -= 1
print(b)

