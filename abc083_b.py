#https://atcoder.jp/contests/abc083/tasks/abc083_b
def sum_s(s:int) -> int:
    """整数sの各桁の和を求める
    :param s: 数字
    :return: sの各桁の合計
    """
    s = str(s)
    s_array = list(map(int, s))
    return sum(s_array)



n, a, b = map(int, input().split())
ans = []
for i in range(1, n + 1):
    sum_array = sum_s(i)
    if sum_array >= a and sum_array <= b:
        ans.append(i)
print(sum(ans))