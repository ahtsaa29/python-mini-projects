# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exp(base, exp):
    pro = 1
    i = 1
    while exp > 0:
        pro = pro * base
        exp = exp - 1
    print(pro)


exp(10, 3)
