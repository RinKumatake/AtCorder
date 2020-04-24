def comparing_strings(a: int, b:int) -> str:
    """整数 a を b 回繰り返してできる文字列と整数 b を a 回繰り返してできる文字列を辞書順比較して小さい方を返す
    :param a: 整数
    :param b: 整数
    :return: 生成した文字列の辞書順比較で小さい方
    """
    a_b_list = []
    a_s = str(a) * b
    b_s = str(b) * a
    a_b_list.append(a_s)
    a_b_list.append(b_s)
    sort_min = sorted(a_b_list)[0]
    return sort_min
    

a, b = map(int, input().split())
print(comparing_strings(a, b))

if __name__ == "__main__":
    assert comparing_strings(4, 3) == "3333", "WA"
    assert comparing_strings(7, 7) == "7777777", "WA"



