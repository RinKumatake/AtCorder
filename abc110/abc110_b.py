# https://atcoder.jp/contests/abc110/tasks/abc110_b

n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
border_x = max(x)
border_y = min(y)
if border_x >= border_y:
    print("War")
elif border_x<= X or border_y>= Y:
    print("War")
else:
    print("No War")

