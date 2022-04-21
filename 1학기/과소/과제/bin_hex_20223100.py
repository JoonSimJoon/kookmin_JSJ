
num_bin=(input())

print(f"Binary number = {num_bin}")
BIT = 4
num_bin = num_bin[::-1]
num_oct = ""
cnt_bit = 0
while cnt_bit < len(num_bin):
    cnt, sum_ = 0, 0
    while cnt < BIT and cnt_bit < len(num_bin):
        sum_ += 2**cnt * int(num_bin[cnt_bit])
        cnt += 1
        cnt_bit += 1
    if(sum_>=10):
        sum_=chr(sum_+55)
    num_oct = str(sum_) + num_oct

print(f"Octal number = {num_oct}")
