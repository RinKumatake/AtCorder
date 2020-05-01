# https://atcoder.jp/contests/abc148/tasks/abc148_c
import fractions
def lcm(a:int, b:int) -> int:
    return (a * b) // fractions.gcd(a, b)

a, b = map(int, input().split())
print(lcm(a, b))

