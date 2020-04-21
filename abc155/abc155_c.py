# https://atcoder.jp/contests/abc155/tasks/abc155_c
import collections

n = int(input())
word = [input() for i in range(n)]
counter = collections.Counter(word)#出てきた言葉と回数が辞書型で返る
rank_word = counter.most_common() #most_common()メソッドを使うことで回数が多い順にタプル型で返る
most_common = rank_word[0][1]
most_common_lst = [i[0] for i in rank_word if i[1] == most_common]#同率１位のワードをリストに
lst = sorted(most_common_lst) #ワードを辞書順に
for i in lst:
    print(i)