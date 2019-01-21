# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_lines = input()

a1,b1 = input_lines.split()

a = int(a1)
b = int(b1)
#print(a)
#print(b)
if a >= 0 and a <= 50 :
    if b >= 1 and b <= 10000 :
        c1 = b + b * a / 100
        print(int(c1))



