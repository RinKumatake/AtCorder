# https://atcoder.jp/contests/abc150/tasks/abc150_c
import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
permutation_list = list(itertools.permutations(p, n)) #タプルで返される
sort_lst = sorted(permutation_list)
x = tuple(p) #検索に使うためリストをタプルに変換
y = tuple(q) 
a = sort_lst.index(x) #一致するタプルを検索してインデックスを返す
b = sort_lst.index(y)
print(abs((a+1)-(b+1)))


