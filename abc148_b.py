def strings_with_the_same_length(n:int, s:str, t:str) -> str:
    """文字列 s, tを１文字づつ交互に出力する
    :param n: s, tの文字数
    :param s: 文字列
    :param t: 文字列
    :return 交互に並べた文字列
    """
    message = []
    for i in range(n):
        message.append(s[i])
        message.append(t[i])
    message_x = "".join(message)
    return message_x

n = int(input())
s, t = input().split()
print(strings_with_the_same_length(n, s, t))

if __name__ == "__main__":
    assert strings_with_the_same_length(2,"ip", "cc") == "icpc", "WA"
    assert strings_with_the_same_length(8,"hmhmnknk", "uuuuuuuu") == "humuhumunukunuku", "WA"