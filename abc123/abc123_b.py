# https://atcoder.jp/contests/abc123/tasks/abc123_b
# 10の倍数ごとにしか注文できない
dishes = [] #調理時間
serve = [] #調理時間が10の倍数とどれだけ離れているか
for i in range(5):
    dish = int(input())
    dishes.append(dish)
    if dish % 10 != 0: 
        time = 10 - dish%10
        serve.append(time)
if serve == []: #提供時間が全て10の倍数ならどの順番に並べても最後の料理が届く時間は同じ
    print(sum(dishes))
else: #提供時間が10の倍数でないのであれば、10の倍数との差を求めて、最大の値となるものを最後に提供することにする。(最大の値以外のものが提供時間に考慮される。)
    sort_serve = sorted(serve)
    sort_serve.remove(sort_serve[len(sort_serve)-1])
    ans = sum(dishes) + sum(sort_serve)
    print(ans)

