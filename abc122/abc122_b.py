# https://atcoder.jp/contests/abc122/tasks/abc122_b

s = input()
counts = []
count = 0
for i in range(len(s)):
    c = s[i:len(s)+1]
    for j in c:
        if "A" in j or "C" in j or "G" in j or "T" in j:
            count += 1
        else:
            break
    counts.append(count)
    count = 0
max_count = max(counts)
print(max_count)    
    

    


