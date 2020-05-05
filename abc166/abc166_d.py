#https://atcoder.jp/contests/abc166/tasks/abc166_d
x = int(input())
lst = []
for i in range(-118, 120):
    for j in range(-119, 119):
        y = i ** 5 - j ** 5
        if y == x:
            lst_1 =[]
            lst_1.append(i)
            lst_1.append(j)
            lst.append(lst_1)
print(lst[0][0], lst[0][1])
            
            


