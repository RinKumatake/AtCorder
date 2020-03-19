def racoon_monster(h: int, a_list: list) -> str:
    """モンスターの体力 h を a_listのダメージを与えられる必殺技で 0以下にできるのか判定して結果を返す
    :param h: モンスターの体力
    :param a_list: a_list[i]の必殺技でモンスターの体力を要素分減らすことができる。
    :return: 体力を0以下にできたかどうかの判定結果
    """ 
    for i in a_list:
        h = h - i
    if h <= 0:
        return "Yes"
    else:
        return "No"

h, n = map(int, input().split())
a_list = list(map(int, input().split()))
print(racoon_monster(h, a_list))

if __name__ == "__main__":
    assert racoon_monster(10, [4, 5, 6]) == "Yes", "WA"
    assert racoon_monster(20, [4, 5, 6]) == "No", "WA"
    assert racoon_monster(210, [31, 41, 59, 26, 53]) == "Yes", "WA"
    assert racoon_monster(211, [31, 41, 59, 26, 53]) == "No", "WA"

