# https://atcoder.jp/contests/abc153/tasks/abc153_c
n, k = map(int, input().split())
h = list(map(int, input().split()))
monster = sorted(h, reverse=True)
surviver = monster[k:len(monster)]
print(sum(surviver))