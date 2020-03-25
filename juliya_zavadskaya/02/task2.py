# task2

'''
#v1
print('Print your list ')
list_task2 = str(input())

new_string = ''
for i in range(len(list_task2)):
    new_string += list_task2[0 - i - 1]
print(new_string)
'''
#v2
print('Print your list ')
list_task2 = str(input())

new_string = ''
for i in range(len(list_task2)):
    new_string = list_task2[::- 1]
print(new_string)
