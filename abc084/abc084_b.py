# https://atcoder.jp/contests/abc084/tasks/abc084_b
a, b = map(int, input().split())
s = input()
s_a = s[0:a]
s_b = s[(a+1):(a+2)+b]
minus = s[a]
if minus == "-" and s_a.isdecimal() and s_b.isdecimal():
    print("Yes")
else:
    print("No")




 
