"""
Jared Singh Sekhon

Homework 5 Question 1

Merge sort and insertion sort implementations from geeksforgeeks and educative at:
https://www.educative.io/answers/merge-sort-in-python
and
https://www.geeksforgeeks.org/python-program-for-insertion-sort/
respectively.
"""
from matplotlib import pyplot as plt
from numpy import random
from copy import deepcopy
import time


# MERGE SORT START ***
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1

# MERGE SORT END ///


# INSERTION SORT START ***
def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

# INSERTION SORT END ///


# Initialize a large array of random numbers
n = 100                                                             # Upper bound of array size

x = []                                                              # X coordinates (array sizes)

merge_y = []                                                        # Y coordinate (mergesort time)
insert_y = []                                                       # Y coordinate (insertionsort time)

for i in range(0, n, 10):                                           # Loop over n times in increments of 10
    x.append(i)                                                     # Add each i to the array of x coordinates

    arr = []

    for k in range(i):                                              # Create an array of i random values
        arr.append(random.random())

    start_time = time.time()                                        # Start the timer for merge sort
    for j in range(100):                                            # Run merge sort 100 times
        mergeSort(deepcopy(arr))
    merge_sort_time = time.time() - start_time                      # Get the completion time of 100 merge sorts
    merge_y.append(merge_sort_time)                                 # Add to merge sort y coordinate aray

    start_time = time.time()                                        # Start the timer for insertion sort
    for j in range(100):                                            # Run 100 times
        insertionSort(deepcopy(arr))
    insertion_sort_time = time.time() - start_time                  # Get completion time
    insert_y.append(insertion_sort_time)                            # Add to insertion sort y coordinate array


plt.plot(x, merge_y, color='Orange', label= 'Merge Sort')           # Plot merge sort graph in orange
plt.plot(x, insert_y, color='Blue', label= 'Insertion Sort')        # Plot insertion sort graph in blue

plt.xlabel('Array Size')                                            # Set x axis as array size

xtick_arr = []
for i in range(0,n,5):                                              # Create an array of ticks incremented by 5
    xtick_arr.append(i)
plt.xticks(xtick_arr)                                               # Set ticks as array of ticks (increments of 5)

plt.ylabel('Runtime (x100)')                                        # Set y label
plt.title('Merge Sort vs. Insertion Sort')                          # Set x label
plt.legend()                                                        # Include graph legend
plt.grid()                                                          # Include the grid for better accuracy

plt.show()                                                          # Display the graph




