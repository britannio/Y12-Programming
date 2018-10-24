# Bubble sort
import random

arrayLen = 15
arrayRange = arrayLen + random.randint(1, 125)

unsorted = random.sample(range(1, arrayRange),arrayLen)  # [random.randint(1,101) for x in range(15)]
counter = -1  # any non-zero value


def swap(index1, index2):
    unsorted[index1], unsorted[index2] = unsorted[index2], unsorted[index1]


print("Unsorted \n" + str(unsorted))
while counter != 0:
    counter = 0
    for x in range(len(unsorted) -1):
        if unsorted[x] > unsorted[x+1]:
            unsorted[x], unsorted[x+1] = unsorted[x+1], unsorted[x]
            counter = counter + 1

print("\nSorted \n" + str(unsorted))

