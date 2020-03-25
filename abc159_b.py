#文字数が奇数であるS（文字列）が回文であるかどうかを判定
def palindrome(s:str)->str:
    #文字列sの長さをnとおく
    s_reverse = s[::-1]     
    x = (len(s) - 1) // 2
    s_1_x = s[:x] #文字列sの1文字目からx文字目までを求める
    s_1_x_reverse = s_1_x[::-1] #1文字目からx文字目までを反転
    y = (len(s) + 3)//2
    s_1_y = s[y - 1:len(s)] #文字列sのy文字目からn文字目まで
    s_1_y_reverse = s_1_y[::-1] #y文字目からn文字目まで       
    
    if s == s_reverse: #sが回文かどうか判定
        if s_1_x == s_1_x_reverse and s_1_y == s_1_y_reverse: #強い回文かどうか判定
            return "Yes"
        else:
            return "No"
    else:
        return "No"

s = input()
print(palindrome(s))