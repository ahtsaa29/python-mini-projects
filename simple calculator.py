a = int(input("please enter first number"))
b = int(input("please enter second number"))
op = input("please enter the operation you wanna perform")

if op == '+':
    print(a+b)

elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)

else:
    print("error")
