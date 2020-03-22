my_str = input('Type string: ')
my_o = []
my_x = []

print('Will return "True" if amount of O and X is equal even if amount is 0. '
      'In other cases will return "False" Not case sensitive.\n')
for i in my_str:

    if i == 'O' or i == 'o':
        my_o.append(i)

    elif i == 'X' or i == 'x':
        my_x.append(i)

if len(my_o) == len(my_x):
    print('True')

else:
    print('False')
