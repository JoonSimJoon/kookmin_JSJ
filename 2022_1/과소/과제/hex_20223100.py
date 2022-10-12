BASE = 16
num_dec=int(input())
print(f"Decimal number = {num_dec}")
num_bin = ""
if num_dec < BASE:
    if(num_dec>=10):
        num_dec=chr(num_dec+55)
    num_bin = num_dec
else:
    while num_dec > 0:
        num_dec, r = num_dec // BASE, num_dec % BASE
        if(r>=10):
            r=chr(r+55)
        num_bin = str(r) + num_bin
print(f"Binary number = {num_bin}") 