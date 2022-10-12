num_str_a,num_str_b = map(str,input().split())

num_bin_a = [int(x) for x in num_str_a]
num_bin_b = [int(x) for x in num_str_b]

num_bin_b = [0] * (len(num_bin_a) - len(num_bin_b)) + num_bin_b

BASE = 2
num_bin = []
carry = 0
bit_index = len(num_bin_a) - 1
carry = 0

while bit_index >= 0:
    bit_a = num_bin_a[bit_index]
    bit_b = num_bin_b[bit_index]
    sum_ = bit_a - bit_b 
    if(sum_<0):
        next_bit_index = bit_index-1
        while True:
            if num_bin_a[next_bit_index]==1:
                num_bin_a[next_bit_index]=0
                break
            else:
                num_bin_a[next_bit_index]=1
                next_bit_index-=1
        sum_=1
    carry, r = sum_ // BASE, sum_ % BASE
    num_bin.insert(0, r)
    bit_index -= 1

if carry:
    num_bin.insert(0, carry)
lnb = len(num_bin)
bit_index=0
while bit_index <lnb:
    if(num_bin[bit_index]==1) or lnb==1:
        answer=num_bin[bit_index:]
        break
    bit_index += 1


print(f"Binary number = {answer}")