__author__ = 'Ksenia'


def binary_search(L, v):
    """Binary search in the ordered list of elements

    :param L: ordered list of elements to search in
    :param v: object fot search
    :return: index of the first occurrence of v in L, or return if l is not in the list
    """

    left_element = 0
    right_element = len(L) - 1
    while left_element <= right_element:
        m = (left_element + right_element) // 2
        if L[m] < v:
            left_element = m + 1
        else:
            right_element = m - 1
    if left_element == len(L) or L[left_element] != v:
        return -1
    else:
        return left_element


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6]
    v = 3
    print(binary_search(L, v))