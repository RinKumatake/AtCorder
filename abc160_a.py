#https://atcoder.jp/contests/abc160/tasks/abc160_a
#与えられた文字列がcoffeeに似ているか判定する。
s = input()
if s[2] == s[3] and s[4] == s[5]:
    print("Yes")
else:
    print("No")