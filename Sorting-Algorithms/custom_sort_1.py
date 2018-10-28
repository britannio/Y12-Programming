import array_gen

# todo start using classes for all algorithms, or nested functions for encapsulation

unsorted = array_gen.random_array(length=15, upper=100, repeats=False)

def bubble_sort(array):
    counter = -1  # any non-zero value
    while counter != 0:
        counter = 0
        for x in range(len(array) - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                counter = counter + 1
    return array

def sort(array):
    upper = len(array)
    middle = len(array) // 2

    array = [bubble_sort(array[:middle]), bubble_sort(array[middle:upper])]
    sorted_array = []
    for x in range(15):
        if array[0] == []:  # is empty
            if array[1] != [] :  # isn't empty
                for x in range(len(array[1])):
                    sorted_array.append(array[1].pop(0))

        elif array[1] == []:  # is empty
            if array[0] != []:  # isn't empty
                for y in range(len(array[0])):
                    sorted_array.append(array[0].pop(0))
        else:
            left = array[0][0]
            right = array[1][0]

            if left < right:
                # move first value from the left to the sorted array
                sorted_array.append(array[0].pop(0))
            else:
                sorted_array.append(array[1].pop(0))

    return sorted_array


print("Unsorted: " + str(unsorted))
print("SORTED" + str(sort(unsorted)))