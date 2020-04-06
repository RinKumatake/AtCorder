import itertools
n = int(input())
d = list(map(int, input().split()))
combination_takoyaki = list(itertools.combinations(d, 2))
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
takoyaki = []
for i in combination_takoyaki:
    i_1 = i[0]
    i_2 = i[1]
    power = i_1 * i_2
    takoyaki.append(power)
takoyaki_power = sum(takoyaki)
print(takoyaki_power)


    



