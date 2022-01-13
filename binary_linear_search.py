import numpy as np
from timeit import default_timer as timer

"""
Performs a sequential search for search_val in vals_list.

Returns the index of the value if found, or -1 if not found.
"""
def sequential_search(vals_list, search_val):
    for i in range(len(vals_list)):
        if vals_list[i] == search_val:
            return i
    return i

"""
Performs a binary search for search_val in vals_list.  It is assumed that vals_list is already sorted.

Returns the index of the value if found, or -1 if not found
"""

def binary_search(vals_list, search_val):
    # implement your algorithm here
    half = vals_list // 2
    list_center = (len(vals_list)) // 2
    center_val = vals_list[list_center]
    if search_val == center_val:
        
    elif search_val < center_val:
        vals_list = vals_list[:half]
    elif search_val > center_val:
        vals_list = vals_list[half:]
    pass

num_items = int(input("How many random list items should be generated? "))
random_list = np.random.randint(low = 0, high = num_items, size = num_items)

val = int(input("What is the value to search for? "))
start = timer()
pos = sequential_search(random_list, val)
end = timer()
print(f"The value {str(val)} occurs at index {str(pos)} in the original random list\nFinding it using a sequential search took {str(end - start)} seconds")

random_list.sort()
start = timer()
#pos = binary_search(random_list, val)
end = timer()
print(f"The value {str(val)} occurs at index {str(pos)} in the sorted list\nFinding it using a binary search took {str(end - start)} seconds")
