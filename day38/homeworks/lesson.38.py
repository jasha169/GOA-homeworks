def manual_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1  # თუ ელემენტი სიაში არ მოიძებნა
