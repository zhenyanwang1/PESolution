import gmpy2
num=gmpy2.mpz("2")
num**=1000
print(sum([int(chr) for chr in str(num)]))