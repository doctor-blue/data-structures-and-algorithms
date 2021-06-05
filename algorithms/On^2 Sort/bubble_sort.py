list = [2, 1, 11, 5, 7, 3, 90, 10, 34, 6,56, 43]

for end in range(len(list)-1, -1, -1):
    for current in range(0, end):
        if list[current] > list[current+1]:
            swap = list[current]
            list[current] = list[current+1]
            list[current+1] = swap
    print(list)
        

print(list)
