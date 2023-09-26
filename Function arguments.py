def add_numbers(a,b):
    result=a+b
    return result
result=add_numbers(10,3)
print(result)

def greet(name,age):
    print(f"Hello,{name}!you are{age}years old.")
greet(age=25,name="Alice")

def greet(name,age=30):
    print(f"Hello,{name}!you are{age}years old.")
greet("Alice")

def add(a, b):
    return a + b
result = add(2, 3)
print(result)

def divide(a,b):
    quotient=a//b
    remainder=a%b
    return quotient,remainder
q,r=divide(10,3)
print("quotient:",q)
print("remainder:",r)

def add_numbers(a,b):
    result=a+b
    return result
result=add_numbers(10,3)
print(result)


