def i_miss_you(s):
    """渡された文字列を全て"x"に置き換えて返す
    :param s: 文字列
    :return: "x"に置き換えた文字列
    """
    string_list = []
    for i in s:
        s_1 = i.replace(i, "x")
        string_list.append(s_1)
    x = "".join(string_list)
    return x

s = input()
print(i_miss_you(s))

if __name__ == "__main__":
    assert i_miss_you("sardine") == "xxxxxxx", "WA"
    assert i_miss_you("xxxx") == "xxxx", "WA"
    assert i_miss_you("panda") == "xxxxx", "WA"