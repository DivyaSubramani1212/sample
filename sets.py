fruits = {"apple", "banana", "orange"}
fruits.add("grape")
fruits.remove("banana")
num_fruits = len(fruits)
print(num_fruits)
more_fruits = {"orange", "grape", "kiwi", "pear"}
common_fruits = fruits.intersection(more_fruits)
print(common_fruits)
diff_fruits = fruits.difference(more_fruits)
print(diff_fruits)
fruits.discard("kiwi")
print(fruits)

