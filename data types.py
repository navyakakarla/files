Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 1
b = 1
print(id(a))
140728236761896
print(id(b))
140728236761896
c = 2
d = 3
print(id(c))
140728236761928
print(id(d))
140728236761960
num =1
num =1
num1 = 1
num2 = 1.1
num3 = 1+2j
print(type(num1))
<class 'int'>
print(type(num2))
<class 'float'>
print(type(num3))
<class 'complex'>
name ="python"
name[0:5:1]
'pytho'
name = "python class"
print(name[::])
python class
print(name[::2])
pto ls
print(name[0:5])
pytho
print(name[:5:])
pytho
print(name[:5:2])
pto
print(name[-1])
s
print(name[::-1])
ssalc nohtyp
print(name[-1:-12:-1])
ssalc nohty
print(name[-1:-13:-1])
ssalc nohtyp
print(name[-1:-13:-1])
ssalc nohtyp
print(name[::-1])
ssalc nohtyp
name ="varaiable"
print(name[::-1])
elbaiarav
>>> a =1
>>> b = 9.9
>>> print(a+b)
10.9
>>> num1 = 100
>>> num2 = "100"
>>> print(num1+num2)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(num1+num2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(num1+int(num2))
200
>>> num1 =10
>>> num2 ="10.2"
>>> print(num1+num2)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(num1+num2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(num1+int(num2))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(num1+int(num2))
ValueError: invalid literal for int() with base 10: '10.2'
>>> print(num1+int(float(num2)))
20
>>> num = 4708848749
>>> number=input("enter 10 digit int")
enter 10 digit int4708848749
>>> print(number)
4708848749
>>> number = input("enter number:",)
enter number:4708848749
>>> print(number[::-2])
97487
>>> print(number[::-1])
9478488074
