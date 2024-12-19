new_lst = [1, 2, 3, 4, 5, 3]
if not new_lst:
    result = 0
else:
    function = sum(new_lst[i] for i in range(0, len(new_lst), 2))
    result = function * new_lst[-1]
print(result)


