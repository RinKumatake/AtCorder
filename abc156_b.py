def digits_156_b(n: int, k:int) -> int:
    """k(10)がn進数の時の桁数を返す
    :param n: 対象となる整数
    :param k: k進数
    :return: K(n)の桁数
    """
    count = 0
    while n > 0:
        n = n // k
        count += 1
    return(count)

n, k = map(int, input().split())
print(digits_156_b(n, k))

if __name__ == "__main__":
    assert digits_156_b(11, 2) == 4, "WA"
    assert digits_156_b(1010101, 10) == 7, "WA"