# https://atcoder.jp/contests/abc108/tasks/abc108_b

x_1, y_1, x_2, y_2 = map(int, input().split())
x = x_2 - x_1
y = y_2 - y_1
x_3 = x_2 - y
y_3 = y_2 + x
x_4 = x_1 - y
y_4 = y_1 + x
print("{} {} {} {}".format(x_3, y_3, x_4, y_4))