list = [9, 4, 10, 3, 5]

for i in range(0, len(list)):
    # print('i =', i)
    lowest = i
    for j in range(i+1, len(list)):
        # print('j=', j)
        if list[lowest] > list[j]:
            lowest = j
    if lowest != i:
        swap = list[i]
        list[i] = list[lowest]
        list[lowest] = swap        

print(list)
 