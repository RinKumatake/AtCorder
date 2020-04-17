# https://atcoder.jp/contests/abc124/tasks/abc124_a

a, b = map(int, input().split())
count = 0
coin = 0
while count < 2:
    if a >= b:
        coin += a
        a -= 1
        count += 1
    elif a <= b:
        coin += b
        b -= 1
        count += 1
print(coin)

        