#円環
k, n = map(int, input().split())
h_list = list(map(int, input().split()))
distance = []
tmp = h_list[0]
for i in range(len(h_list)): #家から次の家までの距離を算出してリストに入れる
    a = h_list[i] - tmp
    distance.append(a)
    tmp = h_list[i]
x = (k - h_list[len(h_list)-1] )+ h_list[0] #N軒目の家から北端までの距離に北端から一軒目の家までの距離を足し合わせてリストに加える。
distance.append(x)
#家から家までの距離を円環状に算出した時に１番長い辺を除いた残りが最短距離
sorted_d_list = sorted(distance)
sorted_d_list.pop()
print(sum(sorted_d_list))


    