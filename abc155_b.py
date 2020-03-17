def papers_please(a_list:list) -> str:
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