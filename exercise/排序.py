def bubble_sort(data_list):
    """
    冒泡排序
    """
    for i in range(len(data_list)):
        for j in range(len(data_list)):
            if data_list[j] > data_list[i]:
                temp = data_list[j]
                data_list[j] = data_list[i]
                data_list[i] = temp
    return data_list


if __name__ == '__main__':
    print(bubble_sort([1, 3, 7, 6, 8, 9, 4, 5, 2]))
