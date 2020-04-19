# https://atcoder.jp/contests/abc117/tasks/abc117_b
n = int(input())
l = list(map(int, input().split()))
sort_l = sorted(l)
sum_n_1 = sum(sort_l[:len(sort_l)-1])
longest = sort_l[len(sort_l)-1]
if longest < sum_n_1:
    print("Yes")
else:
    print("No")

