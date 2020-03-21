def achieve_the_goal(n:int, k:int, m:int, a: list) -> str: 
    """テストの残り１科目で何点取れば目標平均点以上を達成できるのか返す。
    :param n: 科目数
    :param k: 満点の時の点数
    :param m: 目標平均点
    :param a: これまでのテストで取った点数
    :return: 最低取る必要のある点数、又は不可能の場合'-1'
    """

    sum_a = sum(a)
    goal = n * m - sum_a
    if goal > k:
        return '-1'
    elif goal <= 0:
        return 0
    else:
        return goal

n, k, m = map(int, input().split())
a = list(map(int, input().split()))
print(achieve_the_goal(n, k, m, a))