#4
#number = int(input("Enter a number: "))
#if number <= 0:
#   print("Please enter a positive integer.")
#else:
#   print(f"Multiplication table for {number}:")
#for i in range(1, 11):
#       result = number * i
#      print(f"{number} x {i} = {result}")

#5



def multiply_list_items(lst):
    product = 1
    for item in lst:
        product *= item
    return product
my_list = [2, 3, 4, 5]
result = multiply_list_items(my_list)
print("The product of all items in the list is:", result)

