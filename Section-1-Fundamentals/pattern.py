###
''' Response to an array generation and formatting task
    Skills:
        List Comprehension
'''
###

'''array = []; array1 = []
[array.append(0) if x % 2 == 0 else array.append(1) for x in range(10)]
[array1.append(1) if x % 2 == 0 else array1.append(0) for x in range(10)]
[print(array) if x % 2 == 0 else print(array1) for x in range(10)]'''

'''for x in range(10):
    print(array) if x % 2 == 0 else print(array1)'''

'''array = []; array1 = []
[array.append(0) if x % 2 == 0 else array.append(1) for x in range(10)]
[array1.append(1) if x % 2 == 0 else array1.append(0) for x in range(10)]
[print(array) if x % 2 == 0 else print(array1) for x in range(10)]'''

# doesn't work
'''array = []; array1 = []
[[array.append(0) if x % 2 == 0 else array.append(1) for x in range(5)] if y % 2 == 0 else [array1.append(1) if x % 2 == 0 else array1.append(0) for x in range(5)] for y in range(5)]
[print(array) if x % 2 == 0 else print(array1) for x in range(10)]'''

# single dimension array
array = []; array1 = []; array2 = []
[array.append(0) if x % 2 == 0 else array.append(1) for x in range(10)]
[array1.append(1) if x % 2 == 0 else array1.append(0) for x in range(10)]
# [print(array) if x % 2 == 0 else print(array1) for x in range(10)]

# multi dimensional array generation
[array2.append(array) if x % 2 == 0 else array2.append(array1) for x in range(10)];


def print_md_array(md_array):
    # printed without styling
    print(md_array); print()

    # printed neatly
    [print(x) for x in md_array]; print()

    string = ""
    # pretty printed
    for x in md_array: # x looks like [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        for y in x:
            string = string + str(y) + " "#      string.append(str(y) + " ")
        print(string)
        string = ""


print_md_array(array2)

# change the pattern
# array2.append([[x for x in range(10)] for x in range(10)]) # Too many dimensions

# array2 = []
# [array2.append([x for x in range(10)]) for x in range(10)]
# one more line than necessary

array2 = [[x for x in range(10)] for x in range(10)]

print()
print_md_array(array2)
