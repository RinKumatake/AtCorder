import math
a, b, c, d = map(int, input().split())
ta = math.ceil(a/d)
ao = math.ceil(c/b)
if ta >= ao:
    print("Yes")
else:
    print("No")