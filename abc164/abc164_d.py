# https://atcoder.jp/contests/abc164/tasks/abc164_d
s = input()
mod = 2019
mod_lst = [0]*mod
mod_lst[0] =1
x = 0
t = 1
for i in reversed(s): #文字列は左から始まるけど、数字は右から始まる
    x += int(i) * t
    y = x % mod #分配法則 tとiの和のmodはそれぞれのmodを取ったのと同じになる
    t *= 10    
    t %= mod #分配法則 tとiの積のmodはそれぞれのmodを取ったのと同じになる
    mod_lst[y] += 1


count = 0
for j in mod_lst:
    a = j*(j-1)//2
    count += a
print(count)
    
    




