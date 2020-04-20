# https://atcoder.jp/contests/abc111/tasks/abc111_b
n = int(input())
for i in range(111, 1000, 111):
    if i >= n:
        print(i)
        break
    