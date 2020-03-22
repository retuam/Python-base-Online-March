# method 1

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

# method 2

my_str = input('Type string: ')

print('Will return "True" if amount of O and X is equal even if amount is 0. '
      'In other cases will return "False" Not case sensitive.\n')
temp = []
for i in my_str:
    if i == 'O' or i == 'o':
        temp.append(i)

    elif i == 'X' or i == 'x':
        temp.append(i)

if not len(temp):
    print('True')

else:
    print('False')

# method 3

my_str = input('Type string: ')

print('Will return "True" if amount of O and X is equal even if amount is 0. '
      'In other cases will return "False" Not case sensitive.\n')
ls = list(my_str)
test_ls = ['O', 'o', 'X', 'x']
counter = 0
for i in ls:
    if i in test_ls:
        counter += 1
if not counter % 2:
    print('True')
else:
    print('False')