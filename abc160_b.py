#500円硬貨は1000嬉しくて、5円硬貨は5嬉しいとしたら、x円を両替して最大となる嬉しさを求める
x = int(input())
happy_500 = x // 500
happy_5 = (x % 500) // 5
happy = happy_500 * 1000 + happy_5 * 5
print(happy)