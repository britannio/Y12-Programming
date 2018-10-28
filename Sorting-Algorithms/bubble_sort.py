# Bubble sort
import random

arrayLen = 15
arrayRange = arrayLen + random.randint(1, 125)

unsorted = random.sample(range(1, arrayRange),arrayLen)  # [random.randint(1,101) for x in range(15)]

def bubble_sort(array):
    counter = -1  # any non-zero value
    while counter != 0:
        counter = 0
        for x in range(len(array) - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                counter = counter + 1
    return array

print("Unsorted \n" + str(unsorted))


print("\nSorted \n" + str(bubble_sort(unsorted)))

