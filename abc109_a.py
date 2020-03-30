#https://atcoder.jp/contests/abc109/tasks/abc109_a
#今回は条件が1から3までの整数だったので全探索
#奇数になるのは奇数×奇数の時なので、a, bが両方奇数であればYesとなる
a, b = map(int, input().split())
num = []
for i in range(4):    
    if a * b * i % 2 != 0:
        num.append("Yes")
if "Yes" in num:
    print("Yes")
else:
    print("No")
        