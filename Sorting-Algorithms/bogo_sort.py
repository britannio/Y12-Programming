# Bogosort, shuffles items in an array until they are sorted in ascending order
import random

'''
Copyright Brit 2018, don't modify or copy
'''

arrayLen = 11 # My laptop struggles at with an sorting 9 items
arrayRange = arrayLen + random.randint(1, 125)
shuffles = 0
iterations = 0

unsorted = random.sample(range(1, arrayRange), arrayLen)
sortedArray = unsorted
print(unsorted)


def is_sorted(array):
    global iterations
    for index in range(len(array) - 1):
        if array[index] > array[index + 1]:
            iterations = iterations + 1
            return False
    return True


while is_sorted(unsorted) is False:
    random.shuffle(unsorted)
    shuffles = shuffles + 1

print(unsorted)
print("Shuffles: ", str(shuffles))
print("Iterations:", str(iterations))



