def is_sorted_alphabetically(array, is_descending=False):
    sorted_array = sorted(array, reverse=is_descending)
    return array == sorted_array


def is_sorted_by_price(array, is_descending=False):
    sorted_array = sorted(array, reverse=is_descending)
    return array == sorted_array
