# Check Palindrome Number

number = int(input("please enter the number to check: "))

orig_num = number
rev_num = 0

while number > 0:
    reminder = number % 10
    rev_num = (rev_num * 10) + reminder
    number = number // 10
if(orig_num == rev_num):
    print("palindrome")
else:
    print("not palindrome")
