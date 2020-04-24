# https://atcoder.jp/contests/abc102/tasks/abc102_b
n = int(input())
a = list(map(int, input().split()))
print(max(a) - min(a))