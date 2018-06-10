

def max(input_str):
    """Given an integer consisting of 4 digits, we need to maximize it in
    24 hour format. For example, 4372 should return a String of the
    form 23:47, which is the maximum 24 hour value that can be obtained
    from the given integer. Assume the given integer always contains
    exactly 4 digits.

    >>> max('4372')
    '23:47'
    >>> max('9951')
    '19:59'
    >>> max('1234')
    '23:41'
    >>> max('0000')
    '00:00'
    >>> max('0002')
    '20:00'
    >>> max('0204')
    '20:40'
    >>> max('0109')
    '19:00'
    >>> max('2109')
    '21:09'
    >>> max('7642')
    Traceback (most recent call last):
        ...
    ValueError: invalid input
    >>> max('6742')
    Traceback (most recent call last):
        ...
    ValueError: invalid input
    >>> max('7632')
    Traceback (most recent call last):
        ...
    ValueError: invalid input
    """
    digits = sorted([int(it) for it in input_str])

    dec_hour_i = find_max_index(2, digits)
    hour_i = -1
    while dec_hour_i >= 0:
        hour_max = 3 if digits[dec_hour_i] == 2 else 9
        hour_i = find_max_index(hour_max, digits, {dec_hour_i})
        if hour_i >= 0:
            break

        dec_hour_i -= 1

    if any(map(lambda x: x < 0, [hour_i, dec_hour_i])):
        raise ValueError('invalid input')

    exc = {dec_hour_i, hour_i}
    dec_min_i = find_max_index(5, digits, exc)
    if dec_min_i < 0:
        raise ValueError('invalid input')

    exc.add(dec_min_i)
    [min_i] = list(set(range(len(digits))) - exc)
    return '{}{}:{}{}'.format(
        *[digits[i] for i in [dec_hour_i, hour_i, dec_min_i, min_i]])


def find_max_index(val, arr, exc=None):
    """Return index of max element in an array not larger than `val`,
    excluding index `exc` if provided

    >>> find_max_index(1, [1, 2, 3])
    0
    >>> find_max_index(2, [1, 2, 3, 4])
    1
    >>> find_max_index(0, [1, 2, 3, 4])
    -1
    >>> find_max_index(5, [1, 2, 3, 4])
    3
    >>> find_max_index(2, [1, 2, 3, 4], {1})
    0
    >>> find_max_index(3, [1, 2, 3, 4], {1})
    2
    >>> find_max_index(3, [2, 4, 4, 9], {0})
    -1
    """
    index = -1
    for i, el in enumerate(arr):
        if exc and i in exc:
            continue

        if el < val:
            index = i
        elif el == val:
            return i
        else:
            return index

    return index
