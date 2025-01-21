# Define the initial list
courses = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']

# Access and print the first item in the list
print(courses[0])  # Output: 'uli101'

# Modify the first item in the list
courses[0] = 'eac150'
print(courses[0])  # Output: 'eac150'

# Print the updated list
print(courses)  # Output: ['eac150', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']

# Append a new item to the list
courses.append('ops999')
print(courses)  # Output includes 'ops999'

# Insert an item at the beginning of the list
courses.insert(0, 'hwd101')
print(courses)  # Output includes 'hwd101' at index 0

# Remove a specific item from the list
courses.remove('ops335')
print(courses)  # 'ops335' removed from the list

# Sort the list (without altering the original)
sorted_courses = courses.copy()
sorted_courses.sort()
print(sorted_courses)  # Sorted version of the list
