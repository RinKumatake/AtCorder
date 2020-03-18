def papers_please(a_list:list) -> str:
    """渡されたリストが条件（偶数であるものは3または5で割り切れること）を満たすか判定する
    :param a_list: 判定対象のリスト
    :return: 判定結果("APPROVED"/"DENIED")
    """
    approved_list = []      
    for x in a_list:
        if x % 2 == 0:
            if x % 3 == 0 or x % 5 == 0:
                approved_list.append("APPROVED")
            else:
                approved_list.append("DENIED")
        else:
            approved_list.append("APPROVED")
    if "DENIED" in approved_list:
        return("DENIED")
    else:
        return("APPROVED")

n = int(input())
a_list = list(map(int, input().split()))
print(papers_please(a_list))

if __name__ == "__main__":
    assert papers_please([6, 7, 9, 10, 31]) == "APPROVED", "WA"
    assert papers_please([28, 27, 24]) == "DENIED", "WA"