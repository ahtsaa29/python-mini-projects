# Create a new list from a two list using the following condition

list1 = [45, 55, 86, 99, 56]
list2 = [33, 23, 87, 90, 34]

final_list = []

for number in list1:
    if(number % 2 == 1):
        final_list.append(number)

for number in list2:
    if(number % 2 == 0):
        final_list.append(number)

print(final_list)
