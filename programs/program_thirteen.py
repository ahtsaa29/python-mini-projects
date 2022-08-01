# Print multiplication table form 1 to 10

num = int(input("please enter the number for the table: "))

i = 0

for i in range(11):
    print(num, " * ", i, "= ", num*i)
