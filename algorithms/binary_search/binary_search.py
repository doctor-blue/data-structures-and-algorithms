def binary_search(list, value):
    first = 0
    last = len(list)
    return search(list, value, first, last)


def search(list, value, first, last):
    if first > last:
        return None
    size = last - first+1
    midle = first + int(size/2)
   
    if list[midle] is value:
        return midle
    elif list[midle] > value:
        return search(list, value, first, midle)
    else:
        return search(list, value, midle+1, last)