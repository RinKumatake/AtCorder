# https://atcoder.jp/contests/abc147/tasks/abc147_b
def palindrome_philia(s:str) -> int:
    """回文ではない文字列 s を回文にするために1文字選んで任意の文字に変えることができた場合の変える回数を返す
    :param s:文字列
    :return: s を回文にするために文字を変更する回数
    """
    s_r = s[::-1]
    count = 0
    for i in range(len(s)):
        if s[i] != s_r[i]:
            count += 1
    return count // 2
s = input()
print(palindrome_philia(s))

