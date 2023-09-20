#1
#for number in range(1500, 2701):
#  if number % 7 == 0 and number % 5 == 0:
#   print(number)

#2
#word = input("Enter a word: ")
#reversed_word = word[::-1]
#print("Reversed word:", reversed_word)

#3
#for number in range(7):
#   if number == 3 or number == 6:
#       continue
#   print(number)

#4
number = int(input("Enter a number: "))
if number <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

#5
#input_string = 'restart'
#first_char = input_string[0]
#result_string = first_char
#for char in input_string[1:]:
#    if char == first_char:
#       result_string += '$'
#   else:
#       result_string += char
#print("Expected Result:", result_string)

#6
#input_string = input("Enter a string: ")
#if input_string:
#     first_char = input_string[0]
#     modified_string = first_char + input_string[1:].replace(first_char, '$')
#     print("Modified String:", modified_string)
#else:
#    print("Please enter a non-empty string.")

#7
#tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#sorted_list = sorted(tuples_list, key=lambda x: x[-1])
#print(sorted_list)

#8
#input_list = [1, 2, 2, 3, 4, 4, 5]
#result_list = list(set(input_list))
#print("Original List:", input_list)
#print("List with Duplicates Removed:", result_list)

#9
#sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#indices_to_remove = [0, 4, 5]
#result_list = [sample_list[i] for i in range(len(sample_list)) if i not in indices_to_remove]
#print("Original List:", sample_list)
#print("List after Removing Elements:", result_list)

#10
#list1 = ["red", "orange", "green", "blue", "white"]
#list2 = ["black", "yellow", "green", "blue"]
#color1_minus_color2 = [color for color in list1 if color not in list2]
#color2_minus_color1 = [color for color in list2 if color not in list1]
#print("Color1-Color2:", color1_minus_color2)
#print("Color2-Color1:", color2_minus_color1)












