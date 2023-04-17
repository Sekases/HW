my_list = [1, 2, True, False, [1, 2, 3], 'Hello', 'I love python', 2.09, 'Task']

itera = 0
while True:
    if itera == len(my_list):
        break
    if not isinstance(my_list[itera], str):
        del(my_list[itera])
    else:
        itera += 1

print(my_list)