#chr

print(chr(101))
print(ord('e'))

# if
a = 3
if 1 == a:
    print('1')
elif 2 == a:
    print('2')
else:
    print('3')
    print('something else')


b = '1'
if 1 == b:
    print('1')
elif 2 == b:
    print('2')
else:
    print('3')


from time import sleep

for letter in 'my text':
    print(letter, end='')
    sleep(1)

print(letter)


# True and True

# False or False

# XOR

# print('a' and 'b')

a = 'a'
b = 'b'
print(a and b)
if a:
    print(b)
else:
    print(a)
a = False
b = True
print(a or b)
if a:
    print(a)
else:
    print(b)