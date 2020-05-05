n,k = map(int, input().split())
sunuke = []
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    sunuke.append(a)
count_lst=[]
for j in sunuke:
    for a in range(1,n+1):
        if a in j:
            count_lst.append(a)
count=0
for z in range(1, n+1):
    if z not in count_lst:
        count+=1

print(count)

        
