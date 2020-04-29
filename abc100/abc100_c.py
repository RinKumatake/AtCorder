# https://atcoder.jp/contests/abc100/tasks/abc100_c
n = int(input())
a = list(map(int, input().split()))
count_a = []
for i in a:
    count = 0
    while i % 2 == 0:
        i //= 2
        count += 1
    count_a.append(count)
print(sum(count_a))

