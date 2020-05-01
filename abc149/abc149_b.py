def greedy_takahashi(a:int, b:int, k:int) -> str:    
    if a >= k:
        a = a - k 
    elif a + b >= k:    
        k = k - a
        a = 0
        b = b - k    
    else: 
        a = 0
        b = 0
    return "{} {}".format(a, b)
        

a, b, k = map(int, input().split())
print(greedy_takahashi(a, b, k))

if __name__ == "__main__":
    assert greedy_takahashi(2, 3, 3) == "0 2", "WA"
    assert greedy_takahashi(500000000000, 500000000000, 1000000000000) == "0 0", "WA"