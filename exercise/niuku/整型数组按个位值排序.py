int_arr = [123, 356, 654, 920]


def sort_by_last_word(key):
    return int(str(key)[-1])


print(sorted(int_arr, key=sort_by_last_word))
