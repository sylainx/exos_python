#
def min_max_element(tab):
    min = tab[0]
    max = tab[0]
    for i in tab:
        # minimum
        if min > i:
            min = i
        # maximum
        if max < i:
            max = i
    return [min, max]
# End min_max_func


min_and_max = min_max_element([5, 8, 4, 9, 46, -3, 71, -363, 1])
print("min = {} \nmax = {}".format(min_and_max[0], min_and_max[1]))

# maximum element
