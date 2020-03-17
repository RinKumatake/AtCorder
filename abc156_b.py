def digits_156_b(n: int, k:int) -> int:
    count = 0
    while n > 0:
        n = n // k
        count += 1
    return(count)

n, k = map(int, input().split())
print(digits_156_b(n, k))

