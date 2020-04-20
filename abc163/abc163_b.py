n, m = map(int, input().split())
a = list(map(int, input().split()))
homework = sum(a)
dayoff= n - homework
if dayoff < 0:
    print("-1")
else:
    print(dayoff)