import random

# Variable initialisation
pos = random.randint(0, 9 + 1)
weight = 0 if random.randint(1, 10 + 1) >= 5 else 2
array = [1 for x in range(12)]
array[pos] = weight
set1 = array[0:4]
set2 = array[4:8]
set3 = array[8:12]
n1, n2, n3, n4, n5, n6 = array[0], array[1], array[2], array[3], array[4], array[5]
n7, n8, n9, n10, n11, n12 = array[6], array[7], array[8], array[9], array[10], array[11]


def a_sum(arr):
    array_sum = 0
    for item in arr:
        array_sum += item
    return array_sum


def expose(position, heavy):

    index = position - 1
    if heavy:
        print("The item with index " + str(index) + " is a heavy item")
    else:
        print("The item with index " + str(index) + " is a light item")

    print("Original array:")
    print(array)
    print(str(index) + "," + str(array[index]))


if a_sum(set1) == a_sum(set2):
    # set 3 contains the odd item,
    if (n8 + n9) == (n10 + n11):  # (8,9)-(10,11)
        # 12 is odd
        if n12 > 1:
            expose(12, True)
        else:
            expose(12, False)

    elif (n8 + n9) > (n10 + n11):
        # either 9 is heavy or 10/11 are light
        if n10 == n11:
            expose(9, True)
        elif n10 < n11:
            expose(10, False)
        elif n10 > n11:
            expose(11, False)

    elif (n8 + n9) < (n10 + n11):
        # Either 9 is light or 10/11 are heavy
        if n10 == n11:
           expose(9, False)
        elif n10 > n11:
            expose(10, True)
        elif n10 < n11:
            expose(11, True)

elif a_sum(set1) > a_sum(set2):
    # Either set 1 is heavy or set 2 is light
    # But we can't compare either set to set 3(neutral) otherwise 4+ comparisons would be required.
    if n1 + n2 + n5 == n3 + n6 + n9:
        # 4 is heavy or 7/8 are light
        if n7 == n8:
            expose(4, True)
        elif n7 < n8:
            expose(7, False)
        elif n7 > n8:
            expose(8, False)

    elif n1 + n2 + n5 > n3 + n6 + n9:
        # Either 1/2 are heavy or 6 is light
        if n1 == n2:
            expose(6, False)
        elif n1 > n2:
            expose(1, True)
        elif n1 < n2:
            expose(2, True)

    elif n1 + n2 + n5 < n3 + n6 + n9:
        # Either 3 is heavy or 5 is light
        if n5 < n9:
            expose(5, False)
        else:
            expose(3, True)

elif a_sum(set1) < a_sum(set2):
    # Either set 1 is light or set 2 is heavy
    if n5 + n6 + n1 == n7 + n2 + n9:
        # Either 8 is heavy or 3/4 is light
        if n3 == n4:
            expose(8, True)
        elif n3 > n4:
            expose(4, False)
        elif n3 < n4:
            expose(3, False)
    elif n5 + n6 + n1 > n7 + n2 + n9:
        # Either 5/6 are heavy or 2 is light
        if n5 == n6:
            expose(2, False)
        elif n5 > n6:
            expose(5, True)
        elif n5 < n6:
            expose(6, True)
    elif n5 + n6 + n1 < n7 + n2 + n9:
        # Either 7 is heavy or 1 is light
        if n1 == n9:
            expose(7, True)
        else:
            expose(1, False)