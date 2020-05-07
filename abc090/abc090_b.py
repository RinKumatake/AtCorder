# https://atcoder.jp/contests/abc090/tasks/abc090_b
a, b = map(int, input().split())
count = 0
for i in range(a, b+1):
    i = str(i)
    i_reverse = i[::-1]
    if i == i_reverse:
        count += 1
print(count)
