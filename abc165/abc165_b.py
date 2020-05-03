#https://atcoder.jp/contests/abc165/tasks/abc165_b
x = int(input())
chokin = 100
count = 0
while chokin < x:
    chokin = int(chokin *1.01)
    count += 1
print(count)
