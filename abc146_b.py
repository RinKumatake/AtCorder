# https://atcoder.jp/contests/abc146/tasks/abc146_b
def rotn(n:int, s:str) -> str:
    """英大文字からなる文字列の各文字をn文字後の文字に置き換えて出力。ただし "Z" の次は "A"
    :param n: シフトする数
    :param s: 置き換える文字列
    :return: n文字シフトさせて置き換えた結果
    """
    replace_list = []
    a_ascii = ord("A") #Aをascii変換
    for i in s:
        i_ascii = ord(i) + n #各文字をascii変換してn文字分シフトする
        x = i_ascii - a_ascii #A - Z = 25
        if x > 25:
            #ZまできたらAに戻る
            y = x - 26
            replace_i = chr(a_ascii + y)
            replace_list.append(replace_i)
        else:
            replace_i = chr(i_ascii)
            replace_list.append(replace_i)
    replece_string = "".join(replace_list)
    return replece_string

n = int(input())
s = input()
print(rotn(n, s))
