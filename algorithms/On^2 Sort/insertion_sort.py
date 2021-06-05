list = [9, 4, 10, 3,5]

for current in range(1, len(list)):
    for shifting in range(current, 0, -1):
        if list[shifting] < list[shifting-1]:
            swap = list[shifting]
            list[shifting] = list[shifting-1]
            list[shifting-1] = swap
        else:
            break

print(list)
