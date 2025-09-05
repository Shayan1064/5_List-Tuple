# Start with a list
numbers = [1, 2, 3]
print("Original List:", numbers)

# 1. append() → add element at the end
numbers.append(4)
print("After append(4):", numbers)

# 2. extend() → add multiple elements
numbers.extend([5, 6])
print("After extend([5, 6]):", numbers)

# 3. insert() → insert at specific index
numbers.insert(1, 10)   # insert 10 at index 1
print("After insert(1, 10):", numbers)

# 4. remove() → remove first occurrence of a value
numbers.remove(10)
print("After remove(10):", numbers)

# 5. pop() → remove element by index (default last)
numbers.pop()
print("After pop():", numbers)

# 6. clear() → remove all elements
temp = numbers.copy()   # save copy before clearing
numbers.clear()
print("After clear():", numbers)

# 7. copy() → make a copy of list
copy_list = temp.copy()
print("Copy of list:", copy_list)

# 8. sort() → sort in ascending order
copy_list.sort()
print("After sort():", copy_list)

# 9. add → in Python, lists don’t have "add()", 
#          we use append() for single item or extend() for multiple.
