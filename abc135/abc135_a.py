# https://atcoder.jp/contests/abc135/tasks/abc135_a

a, b = map(int, input().split())
#aとbの偶奇が異なる時にはどのような整数Kでも偶奇は異なるままとなるのでIMPOSSIBLEとなる
x = a + b
if x % 2 == 0: # a % 2 == b % 2 の方が適切かもしれない
    print(x // 2)
else:
    print("IMPOSSIBLE")
