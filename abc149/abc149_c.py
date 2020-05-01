# https://atcoder.jp/contests/abc149/tasks/abc149_c

def is_prime(x:int) -> bool:
    """
    整数xが素数であるか判定
    :param x: 整数
    :return:bool値
    """
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True


x = int(input())
while is_prime(x) == False:
    x += 1
print(x)


if __name__ == "__main__":
    assert is_prime(11)== True, "WA"
    assert is_prime(10) == False, "WA"
    assert is_prime(1) == False, "WA"
