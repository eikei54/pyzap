# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_lines = input()
num_address = int(input_lines)
print("input:", num_address)
if (num_address < 1) or (num_address > 100):
    print("False")

count = 1
while count <= num_address:
    count += 1
    addr = input()
    #print(len(addr))
    if len(addr) != 7:
        #print("len is not 7")
        print("False", len(addr))
        continue
    for num in addr.split('.'):
        if not num:
            print("No string", num)
            break
        else:
            if (int(num) < 0) or (int(num) > 255):
                print("False:", num)
                break
            #print("check type", type(num))
    print("Check Passed: ", addr)
    #print("True")
    #print("False")

def chk_addr(hoge):
    #if hoge.
    return "NG"
    #return "OK"
