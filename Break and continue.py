numbers=[15,22,17,30,27,24,21]
for num in numbers:
if num<=20:
continue
if num%2==0:
print("First even number greater than 20:",num)
break