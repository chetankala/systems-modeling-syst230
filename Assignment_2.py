''' Write a program that ask several users, and once the user enter "done"
    compute and print out the minimum, maximum, and average numbers '''

number = input("Enter a number: ")
num_string = list()
num_string.append(number)  # Append the first number into the list
i = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    i = i + 1
    num_string.append(number)   # Add the rest of the numbers to the list
    
num_list = list(num_string)
final_list = []

# Convert the strings inside the list to integers
for i in num_list:
    a = int(i)
    final_list.append(a)   # Add integers to new list
    
max_val = max(final_list)                        # Calculating maximum value
min_val = min(final_list)                        # Calculating minimum value
Average = sum(final_list) / len(final_list)      # Calculating average value 

print("Maximum: ", max_val)
print("Minimum: ", min_val)
print("Average: ", Average)

