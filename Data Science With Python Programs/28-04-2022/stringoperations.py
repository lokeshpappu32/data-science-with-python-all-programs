Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c=1+7*3/3*4/5
>>> print(c)
6.6
>>> c=1+2*3/3*4/5
>>> print(c)
2.6
>>> c=-10%3
>>> print(c)
2
>>> c=-10%-3
>>> print(c)
-1
>>> c=10%-3
>>> print(c)
-2
>>> a="python"
>>> a.upper()
'PYTHON'
>>> b="Langauage"
>>> print(a+b)
pythonLangauage
>>> print(a+" "+b)
python Langauage
>>> print("str is :",a+" "+b)
str is : python Langauage
>>> print(b[5])
u
>>> a.toupper()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.toupper()
AttributeError: 'str' object has no attribute 'toupper'
>>> a.isupper()
False
>>> print(a[2;5])
SyntaxError: invalid syntax
>>> print(a[2:5])
tho
>>> a.isdigit()
False
>>>a.isalpha()
False
