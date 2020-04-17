# https://atcoder.jp/contests/abc126/tasks/abc126_b

s = int(input())
s_1 = s // 100 #4桁の数字列の上2桁を取り出す
s_2 = s % 100  #4桁の数字列の下2桁を取り出す

if 1 <= s_1 <=12 and 1 <= s_2 <= 12:
    print("AMBIGUOUS")
elif 1 <= s_1 <= 12:
    print("MMYY")
elif 1 <= s_2 <= 12:
    print("YYMM")
else:
    print("NA")