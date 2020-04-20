n = int(input())
price=[int(input()) for i in range(n)]
sort_price = sorted(price)
discount = sort_price[len(sort_price)-1] // 2
sort_price[len(sort_price)-1] = discount
print(sum(sort_price))

