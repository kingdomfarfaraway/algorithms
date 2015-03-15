__author__ = 'Ksenia'


def linear_search(L, v):
    """Linear search in the list of elements

    :param L: list of elements to search in
    :param v: object fot search
    :return: index of the first occurrence of v in L, or return if l is not in the list
    """

    i = 0
    while i != len(L) and L[i] != v:
        i += 1
    if i == len(L):
        return -1
    else:
        return i


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    v = 5
    print(linear_search(L, v))
