# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 11/24/2018
# Lab 5 purpose: practice the use of Heaps


# Implementation of Heap Data Structure
class Heap:

    def __init__(self):
        self.heap_array = []

    # method fixes a newly inserted item from bottom to top of tree
    def fix_up(self, i):
        while (i-1) // 2 > -1:  # Checks through the whole array
            if self.heap_array[i] < self.heap_array[(i-1) // 2]:
                # Swap
                temp = self.heap_array[(i-1) // 2]
                self.heap_array[(i-1) // 2] = self.heap_array[i]
                self.heap_array[i] = temp
            i = (i-1) // 2

    # Inserts new item to heap
    def insert(self, k):
        self.heap_array.append(k)
        self.fix_up(len(self.heap_array) - 1)

    # Returns smallest element in Heap
    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array[0]

        # Sets root to the last element in heap array
        self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]
        self.heap_array.pop()
        # Calls method to keep heap property
        self.fix_down(0)

        return min_elem

    # Method fixes a heap array from top to bottom
    def fix_down(self, i):
        while ((i+1) * 2) - 1 <= (len(self.heap_array) - 1):  # Continues through whole array
            min_child = self.min_child_index(i)  # Method returns the index of smallest children
            if self.heap_array[i] > self.heap_array[min_child]:
                # Swap
                temp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[min_child]
                self.heap_array[min_child] = temp
            i = min_child

    # Method returns the index of the smallest children
    def min_child_index(self, i):
        # Checks if there is only a left child
        if ((i+1)*2) > len(self.heap_array) - 1:
            return ((i+1) * 2) - 1
        else:
            # Compares both children and returns index to smallest one
            if self.heap_array[((i+1) * 2) - 1] < self.heap_array[(i+1)*2]:
                return ((i+1) * 2) - 1
            else:
                return (i+1)*2

    # Checks if Heap is empty
    def is_empty(self):
        return len(self.heap_array) == 0

    # Prints every value in the Heap
    def print_heap(self):
        for i in self.heap_array:
            print(i)
        return
