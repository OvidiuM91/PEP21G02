name = 'Jhon'
age = 26

print('name: ', name, ', age: ', age)

# print = 'print'
#
# print('name: ', name, ', age: ', age)

# type function

result = type(name)
print(result)

result = type(age)
print(result)


print(5*name)
result1=5*name
result2=type(result1)
print(result2)


result = id(name)
print(result)


print(8 + 8)
print((8).__add__(8))

print(8 * ' text')
print(' text' * 8)

print((8).__mul__ (' text'))
print((' text').__mul__(8))

print(8 - 8)
print((8).__sub__(8))

print(8 / 8)
print((8).__truediv__(8))


print(8 ** 8)
print((8).__pow__(8))
print(pow(8, 8))


# Float

result3=8/8
result4=type(result3)
print(result4)
print(type(result3))


a=3
b=4
c=5
x=(-b+(b**2-4*a*c)**(1/2))/(2*a)
# x=(-b-(b**2-4*a*c)**(1/2))/(2*a)
print(x)

nr = 1.1.__pow__(2)

bsqr= b.__pow__(2)
multi= (4).__mul__(a.__mul__(c))
dif= bsqr.__sub__(multi)
dif=float(dif)
var=(1).__truediv__(2)
rad=dif.__pow__(var)
b= complex(b)
dif2=(-b).__sub__(rad)
mul1=(2).__mul__(a)
ec= dif2.__truediv__(mul1)
print(ec)


# Complex

nr1 = 1.0 + 1.0j
nr2 = 3 + 5j
print(type(nr1))
print(nr1+ nr2)


# Strings
my_str1 = 'My String \n no multi line'
print(my_str1)
my_str2 = '''this
is
a
multi
string'''
print(my_str2)
my_str3 = r"My String \n no multi line"
print(my_str3)

my_str4 = f"""My String {my_str2}"""
print(my_str4)


# dir
info = dir(my_str4)
print(info)

var1 = 'this is {}'
cap = var1.capitalize()
print(cap)
format1 = var1.format('Sparta')
print(format1)

phone = "0747.655.444"
split1 = phone.split("7")
print(split1)
split2 = phone.split(sep = ".", maxsplit=1)
print(split2)


# input
# name = input('Give me your name: ')

# print(var1, input('Give me your name: '))

# slice
text="My Text"
first_letter = "My Text"[0]
print(first_letter)
slice1 = text[1:4]
print(slice1)
slice2 = text[0:7:2]
print(slice2)

#text1 = input('Enter text here: ')
#slice3 = text1[0:5]
#slice4 = text1[5:11]
#print(slice3)
#print(slice4)
#print(slice4+slice3)


# negative step
#reverse = text[::-1]
#print(reverse)
#reverse1 = slice3[::-1]
#reverse2 = slice4[::-1]
#print(reverse2 + reverse1)


# True, False

my_bool = True
print(type(my_bool))
my_bool = False
print(type(my_bool))

print(id(True))
print(id(False))
print(id(10))

print(True + False)
print(dir(True))
print(True.__add__(False))

# None
my_none = None
x = print('')
print(x)

# Truth

# 0 -> False
# 'a' -> True
# '' -> False
# None -> False

print(bool(0+0j))
print(bool(0.0))