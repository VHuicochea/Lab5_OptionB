# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 11/24/2018
# Lab 5 purpose: practice the use of Heaps

import random
from Heap import Heap


# Method receives an array and sorts it using a Heap
def heap_sort(array):
    h = Heap()
    for i in range(len(array)):
        h.insert(array[i])

    sorted = []

    for i in range(len(h.heap_array)):
        sorted.append(h.extract_min())

    return sorted


# Method generates an array filled with random integers from 0 to 100
def get_array(size):
    array = []

    try:
        for i in range(int(size)):
            array.append(random.randint(0, 100))

        return array
    # Catches if input from user is not an Integer
    except ValueError:
        print("Please enter an integer.")


# Main method
def main():
    keep_going = True
    while keep_going:
        print("Welcome, this program will sort a randomly-generated array using a Heap.")
        print()
        print("Please enter the size for the randomly generated array:")
        answer = input()

        # Generates the array with the size provided by user
        user_array = get_array(answer)

        if user_array is not None:
            print("This is the array before sorting: ")
            # Prints original array
            for i in user_array:
                print(i, sep=' ', end='', flush=True)
                print(" ", sep=' ', end=' ', flush=True)

            print("\nSorting your array...")

            # Sorts the array
            sorted_array = heap_sort(user_array)

            print("This is your sorted array:")

            # Prints sorted array
            for i in sorted_array:
                print(i, sep=' ', end='', flush=True)
                print(" ", sep=' ', end=' ', flush=True)

            print()

        loop = input("\nWould you like to perform a new operation? y/n\n")

        if loop == 'y':
            keep_going = True
        elif loop == 'n':
            keep_going = False
        else:
            print("You typed a non-supported command, please try again.")


main()