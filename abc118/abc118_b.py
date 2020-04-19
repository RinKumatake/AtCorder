# https://atcoder.jp/contests/abc118/tasks/abc118_b

n, m = map(int, input().split())
servey = []
for i in range(n):
    k_a = list(map(int, input().split()))
    servey.append(k_a)
for j in servey:
    del j[0]
loves = []
for x in range(1, m+1):
    count = 0
    for y in servey:
        if x in y:
            count+=1
        loves.append(count)
food_count = 0     
for z in loves:
    if z == n:
        food_count += 1

print(food_count)






