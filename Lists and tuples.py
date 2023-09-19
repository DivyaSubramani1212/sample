my_list=[1,2,3,4,5]
print(my_list)

my_list=['apple','banana','cherry']
print(my_list[0])
print(my_list[-1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

my_tuple=(1,2,3,'a','b','c')
print(my_tuple[0])
print(my_tuple[3])
print(my_tuple[1:4])
print(my_tuple[:3])
print(my_tuple[3:])
print(len(my_tuple))
tuple1=(1,2,3)
tuple2=('a','b','c')
concatenated_tuple=tuple1+tuple2
print(concatenated_tuple)
repeated_tuple=(1,2)*3
print(repeated_tuple)
tuple3=('John','Doe',25)
first_name,last_name,age=tuple3
print(first_name)
print(last_name)
print(age)

my_tuple=(1,2,3)
print(my_tuple[1])
print(my_tuple[1:3])
print(len(my_tuple))
my_tuple2=(4,5,6)
concatenated_tuple=my_tuple+my_tuple2
print(concatenated_tuple)
repeated_tuple=my_tuple*2
print(repeated_tuple)
a,b,c=my_tuple
print(b)