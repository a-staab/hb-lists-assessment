"""List Assessment

Edit the functions until all of the doctests pass when
you run this file.
"""


def get_odd_nums(numbers_list):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> get_odd_nums([1, 2, 7, -5])
        [1, 7, -5]

        >>> get_odd_nums([2, -6, 8])
        []
    """
    odd_numbers = [num for num in numbers_list if num % 2 != 0]
    return odd_numbers


def print_index(items_list):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_index(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_index(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
    """
    for number in range(len(items_list)):
        print "%d " % (number) + str(items_list[number])


def get_foods_in_common(foods_list_1, foods_list_2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> get_foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']

    If there are no foods in common, return an empty list::

        >>> get_foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """
    foods_in_common = sorted(list(set(foods_list_1) & set(foods_list_2)))
    return foods_in_common


def skip_every_second(items_list):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> skip_every_second([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> skip_every_second(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    every_other_item = items_list[::2]
    return every_other_item


def print_n_largest(items_list, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> print_n_largest([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> print_n_largest([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> print_n_largest([3, 3, 3, 2, 1], 2)
        [3, 3]
    """
    ascending_nums = sorted(items_list)
    if n != 0:
        return ascending_nums[-n:]
    else:
        return []


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
