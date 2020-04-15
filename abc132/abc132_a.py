# https://atcoder.jp/contests/abc132/tasks/abc132_a

s = input()
variety = set(s)
if len(variety) == 2:
    x = []
    for i in variety:
        x.append(i)
    count_1 = s.count(x[0])
    count_2 = s.count(x[1])
    if count_1 == count_2:
        print("Yes")
    else:
        print("No")
else:
    print("No")

    

