# https://atcoder.jp/contests/abc103/tasks/abc103_b

s = input()
t = input()

s_lst = [i for i in s]
ans = 0
for i in range(len(s_lst)):
    tmp = s_lst[len(s_lst)-1]
    s_lst.pop()
    a = []
    a.append(tmp)
    for j in s_lst:
        a.append(j)
    s_lst = a
    b = "".join(a)
    if b == t:
        ans += 1
if ans >=1:
    print("Yes")
else:
    print("No")

#別解答
for i in range(len(s)):
    if s == t:
        print("Yes")
        break
    else:
        s = s[-1]+s[:-1]
else:
    print("No")



