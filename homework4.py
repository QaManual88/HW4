first_lst = [0, 1, 3, 0, 4, 5]
non_zero = []
zero = []

for num in first_lst:
    if num != 0:
        non_zero.append(num)
    else:
        zero.append(num)

result = non_zero + zero
print(result)

