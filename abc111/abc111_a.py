# https://atcoder.jp/contests/abc111/tasks/abc111_a

n = input()
swap_n = []
for i in n:
    if i == "1":
        i = "9"
        swap_n.append(i)
    elif i == "9":
        i = "1"
        swap_n.append(i)
    else:
        swap_n.append(i)
num = "".join(swap_n)
print(int(num))   



    