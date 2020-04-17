# https://atcoder.jp/contests/abc126/tasks/abc126_a

n, k = map(int, input().split())
s = input()
s_1 = s[k-1]
s_low = s_1.lower()
s_new = [i for i in s]
s_new[k-1] = s_low

print("".join(s_new))
