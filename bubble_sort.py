import numpy as np
from timeit import default_timer as timer

"""
This function performs a bubble sort on unsorted_list.
Upon exit, unsorted_list should be sorted.
"""

def bubble_sort(unsorted_list):
    # code here

    pass

num_items = int(input("How many random list items should be generated? "))
random_list = np.random.randint(low = -num_items, high = num_items, size = num_items).tolist()
print(f"Here's the original list\n{random_list}")
start = timer()
bubble_sort(random_list)
end = timer()
print(f"Sorting took {str(round(end - start), 2)} seconds")
print(f"Here's the sorted list\n{random_list}")
