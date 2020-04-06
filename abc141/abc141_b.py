s = input()
s1 = s[0:len(s):2]
s2 = s[1:len(s):2]
if "L" in s1 or "R" in s2:
    print("No")
else:
    print("Yes")