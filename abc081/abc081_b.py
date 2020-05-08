# https://atcoder.jp/contests/abc081/tasks/abc081_b
n = int(input())
a = list(map(int, input().split()))
count = 0
odd = 0
while odd == 0:
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
        else:
            odd += 1
    count+=1

print(count-1)    


