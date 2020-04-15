# https://atcoder.jp/contests/abc131/tasks/abc131_a
s = input()
count = 0
for i in range(3):
    if s[i] == s[i+1]:
        count+=1
if count > 0:
    print("Bad")
else:
    print("Good")
        