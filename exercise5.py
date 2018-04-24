a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_overlap(list1, list2):
    new_list = []
    new_lilst_2 = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                new_list.append(item1)
    return new_list

print(list_overlap(a, b))
