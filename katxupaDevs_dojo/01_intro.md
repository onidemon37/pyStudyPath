#!/usr/bin/python3.7

print("Hello world!")

# Variables
idade = 30
print(" idade =", idade)
print("Di li 10 ano, bu ta teni", idade + 10)

print(idade + 10)

# Operators
# "+" "-" "*" "/" "//" "%" "**"

x = 10
y = 23

print('x + y =', x+y)
print('x - y =', x-y)
print('x * y =', x*y)
print('x / y =', x/y)
print('x // y =', x//y)
print('x % y =', x%y)
print('x ** y =', x**y)

# assignenment operators
x = 10

x += 5 == 15
x -= 5 == 5
x /=5 == 2


# get Input from User
name = input('Enter bu name:')
idade = int (input ("digite um numero: "))

print("My name is: ", name "e nha numero e: ", numero)
name = str (input (""))


# Comments na python
#  3 forma di fazi comment

# keli e um comment

"""
    This is a multi
    line comment
    weuhfwe w.
"""

'''
    This is also
    a multiline
    comment.
'''

# Type conversion
# The process of converting the value of one data type (integer,
# string, float, etc.) to another is called type conversion.
# Python has two types of type conversion.

idade = 40
altura = 1.68

novo_numero = idade + altura

print("novo numero =", novo_numero)
print("datatype of novo_numero: ", type(novo_numero))


# Python cannot convert strint to int, or int to string
idade = 10
str_idade = "50"

print (idade+str_idade)
# nu ta tem error na es caso li
#Python ta cuspi kel seginte erro li

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

# Explicit conversion
## You convert the datatype
