# https://atcoder.jp/contests/abc151/tasks/abc151_c
import collections
n, m = map(int, input().split())
wa = []
submission = set()
for i in range(m):   
    p, s = input().split()
    if p in submission:
        continue

    if s == "AC":
        submission.add(p)
    else:
        wa.append(p)
wa_count = collections.Counter(wa)
pena = 0
for j in submission:
    x = wa_count[j]
    pena += x

print(len(submission), pena)









 



    
