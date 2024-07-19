import random


def random_choice_items(total_items_count, max_number_of_random_items):
    result = []
    while len(result) < max_number_of_random_items:
        random_num = random.randint(0, total_items_count-1)
        if random_num not in result:
            result.append(random_num)
    return result

