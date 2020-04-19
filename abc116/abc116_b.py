# https://atcoder.jp/contests/abc116/tasks/abc116_b
# 最終的には4->2->1の循環になるので、4,2,1が出た項+3すれば答えが得られる
s = int(input())
if s == 1 or s == 2 or s == 4: #初項で4, 2, 1のどれかが出たら+3したの4項目に同じ数字が現れる
    print(4)
else:
    count = 1
    while s!=4:
        if s % 2 == 0:
            s = s//2
            count += 1
        else:
            s = 3 * s + 1
            count += 1
    print(count+3)
