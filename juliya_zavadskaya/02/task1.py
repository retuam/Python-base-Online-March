# task1
# 1

user_list = []
character_o = []
character_x = []

new_element = input('Print your list ')
user_list.append(new_element)
print(user_list)
for i in user_list:
    if i == 'O' or 'o':
        character_o.append(i)

    elif i in user_list:
        if i == 'X' or 'x':
            character_x.append(i)

if character_o == character_x:
    print('True')
else:
    print('False')

# 2


import length as length
user_list_2 = []
sum_list = []

new_element_2 = input('Print your list ')
user_list_2.append(new_element_2)

for i in user_list_2:
    if i == 'O' or 'o' or 'X' or 'x':
        sum_list.append(i)
if len(sum_list) % 2:
    print('False')
else:
    print('True')
