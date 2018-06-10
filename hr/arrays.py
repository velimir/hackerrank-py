

def find_unsorted_len(arr):
    """Find maximum unsorted subarray

    >>> find_unsorted_len([2, 6, 4, 8, 10, 9, 15])
    5
    >>> find_unsorted_len([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60])
    6
    >>> find_unsorted_len([0, 1, 15, 25, 6, 7, 30, 40, 50])
    4
    >>> find_unsorted_len([1, 2, 3, 4])
    Traceback (most recent call last):
        ...
    ValueError: sorted array
    >>> find_unsorted_len([])
    Traceback (most recent call last):
        ...
    ValueError: sorted array
    >>> arr = [1, 2, 3, 4]
    >>> sub_len = find_unsorted_len(sorted(arr, reverse=True))
    >>> sub_len == len(arr)
    True
    """
    # import pdb; pdb.set_trace()
    min_el = None
    prev = None
    for el in arr:
        if el < (prev or el):
            min_el = min(min_el or el, el)
        prev = el

    max_el = None
    prev = None
    for el in arr[::-1]:
        if el > (prev or el):
            max_el = max(max_el or el, el)
        prev = el

    if not any([min_el, max_el]):
        raise ValueError('sorted array')

    for i, el in enumerate(arr):
        if el > min_el:
            min_index = i
            break

    for i, el in enumerate(arr[::-1]):
        if el < max_el:
            max_index = (len(arr) - 1) - i
            break

    return max_index - min_index + 1
