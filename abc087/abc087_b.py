# https://atcoder.jp/contests/abc087/tasks/abc087_b
a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0
for i in range(a+1):
    p = i*500
    for j in range(b+1):
        q = j * 100
        for k in range(c+1):
            r = k * 50
            if p+q+r == x:
                count+=1           
                
print(count)
