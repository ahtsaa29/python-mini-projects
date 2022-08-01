# Write a Program to extract each digit from an integer in the reverse order.

from math import remainder


number = int(input("Enter a number: "))
rev_num = 0

while number > 0:
    rem = number % 10
    rev_num = (rev_num * 10) + rem
    number = number // 10

print(rev_num)
