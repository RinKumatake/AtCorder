# https://atcoder.jp/contests/abc088/tasks/abc088_b
n = int(input())
a = list(map(int, input().split()))
sort_a = sorted(a, reverse=True)
alice = [sort_a[i] for i in range(n) if i%2==0]
bob = [sort_a[i] for i in range(n) if i%2!=0]
point_alice = sum(alice)
point_bob = sum(bob)
print(point_alice - point_bob)