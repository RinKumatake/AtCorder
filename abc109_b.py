# https://atcoder.jp/contests/abc109/tasks/abc109_b
def has_duplicates(words:list) -> bool:
    """リストの中に重複している要素がないかチェック
    :param words: 単語のリスト
    :return: 判定結果(True/False)
    """
    return len(words) != len(set(words))

def words(n:int) -> list:
    """与えられた繰り返し回数に対して、単語をリストに入れる
    :param n: しりとりの繰り返し回数
    :return:単語リスト
    """
    words = []
    for i in range(n):
        w = input()
        words.append(w)
    return words

def shiritori(shiritori_words:list) -> list:
    """与えられたリストでしりとりが成立してることを判定する。
    :param shiritori_words: しりとりの単語リスト
    :return: それぞれの単語に対する判定結果をリストにしたもの
    """
    ans = []
    word = shiritori_words[0]
    end_word = word[len(word) -1]
    for j in range(1, len(shiritori_words)):
        word = shiritori_words[j]
        first_word = word[0]
        if has_duplicates(shiritori_words) or end_word != first_word:
            ans.append("No")
        else:
            ans.append("Yes")
        end_word = word[len(word) - 1]
    return ans
            
        

n = int(input())
shiritori_words = words(n)
ans = shiritori(shiritori_words)
if "No" in ans:
    print("No")
else:
    print("Yes")

