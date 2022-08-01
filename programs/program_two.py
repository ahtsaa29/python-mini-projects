# Print the sum of the current number and the previous number

# Fibonacci series

previous_number = 0
current_number = 0

for number in range(10):

    print("Previous number is ", previous_number, "current nnumber is:",
          current_number, "\nAnd their sum is ", previous_number+current_number)
    previous_number = current_number
    current_number = previous_number+1
