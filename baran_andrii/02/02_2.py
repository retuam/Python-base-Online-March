# Method 1
print('METHOD 1')
my_str = 'Hello'
new_str = ''

for i in range(len(my_str)):
    new_str += my_str[0 - i - 1]

print(new_str)

# Method 2
print('METHOD 2')
my_str = 'Hello'
new_str = ''

for i in range(len(my_str)-1, -1,  -1):
    new_str += my_str[i]
print(new_str)

# Method 3

print('METHOD 3')

my_str = 'Hello'
my_ls = list(my_str)
res_str = ''
for i in range(len(my_str)-1, -1, -1):
    res_str += my_ls[i]

print(str(res_str))