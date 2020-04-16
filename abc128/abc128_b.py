# https://atcoder.jp/contests/abc128/tasks/abc128_b

n = int(input())
guide = []
for i in range(n):
   #レストラン 
   restaurant = []
   s, p = input().split()
   #点数をintに変換
   p_1 = int(p)
   #街の名前と点数をそれぞれレストランに入れる
   restaurant.append(s)
   restaurant.append(p_1) 
   #レストラン番号を生成して、レストランに入れる
   x = i+1
   restaurant.append(x)
   #レストランをガイドに入れる
   guide.append(restaurant) 
#指定された通りにソートする
sort_guide = sorted(guide, key=lambda x:(x[0],-x[1]))
#レストラン番号はガイドリスト（２次元配列）の[i][2]に入っている
for i in range(len(sort_guide)):
    print(sort_guide[i][2])

