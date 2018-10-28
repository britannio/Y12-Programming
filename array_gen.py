import random


def random_array(length=2, upper=100, repeats=False):

    if repeats:
        return [random.randint(0, upper + 1) for x in range(length)]
    else:
        if upper >= length:
            return random.sample(range(0, upper + 1), length)
        else:
            return []


