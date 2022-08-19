Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=[1,2,3,4]
>>> st=["hi","hwllo"]
>>> B=[1,"jo"]
>>> A[3]
4
>>> B[1]
'jo'
>>> print(A)
[1, 2, 3, 4]
>>> print(A[1])
2
>>> A[-1]
4
>>> A[-6]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    A[-6]
IndexError: list index out of range
>>> A[0:3]
[1, 2, 3]
>>> A[0:4]
[1, 2, 3, 4]
>>> A[0:6]
[1, 2, 3, 4]
>>> A[0:]
[1, 2, 3, 4]
>>> A[-1:-3]
[]
>>> A[-1:]
[4]
>>> A[-1:-2]
[]
>>> A1=A+B
>>> A1
[1, 2, 3, 4, 1, 'jo']
>>> '''Update functions'''
'Update functions'
>>> A.insert(4,10)
>>> A
[1, 2, 3, 4, 10]
>>> A.extend([9,8,7])
>>> A
[1, 2, 3, 4, 10, 9, 8, 7]
>>> A.append([10,11,12])
>>> A
[1, 2, 3, 4, 10, 9, 8, 7, [10, 11, 12]]
>>> A[3]
4
>>> A[8]
[10, 11, 12]
>>> #remove function using indexing and its value
>>> A.remove(9)
>>> A
[1, 2, 3, 4, 10, 8, 7, [10, 11, 12]]
>>> #Using indexing
>>> A.remove(A[2])
>>> A
[1, 2, 4, 10, 8, 7, [10, 11, 12]]
>>> #using pop
>>> A.pop(7)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    A.pop(7)
IndexError: pop index out of range
>>> A.pop(4)
8
>>> A
[1, 2, 4, 10, 7, [10, 11, 12]]
>>> #modify functuon
>>> #Changing the value of the Loist
>>> A[1]=10
>>> A
[1, 10, 4, 10, 7, [10, 11, 12]]
>>> A[1:2]=["A","B"]
>>> A
[1, 'A', 'B', 4, 10, 7, [10, 11, 12]]
>>> A[1:2]=["Aa","Bb","Cc"]
>>> A
[1, 'Aa', 'Bb', 'Cc', 'B', 4, 10, 7, [10, 11, 12]]
>>> A[1:2]=["Aa","Bb","Cc","Dd"]
>>> A
[1, 'Aa', 'Bb', 'Cc', 'Dd', 'Bb', 'Cc', 'B', 4, 10, 7, [10, 11, 12]]
>>> A.sort()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    A.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> B.sort()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    B.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> st.sort()
>>> ST
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    ST
NameError: name 'ST' is not defined
>>> st
['hi', 'hwllo']
>>> st.sort(reverse:True)
SyntaxError: invalid syntax
>>> st.sort(reverse=True)
>>> st
['hwllo', 'hi']
>>> st.reverse
<built-in method reverse of list object at 0x033EA2E8>
>>> st.reverse()
>>> st
['hi', 'hwllo']
>>> st
['hi', 'hwllo']
>>> D1=[10,20,30]
>>> d=D1
>>> d
[10, 20, 30]
>>> D1[2]=22
>>> d
[10, 20, 22]
>>> #above example shows referencing same data using same location
>>> #copy is different from referencing
>>> D1.count(10)
1
>>> D1.append([11,22,33])
>>> D1
[10, 20, 22, [11, 22, 33]]
>>> D1.remove(22)
>>> D1
[10, 20, [11, 22, 33]]
>>> D1.pop()
[11, 22, 33]
>>> D1
[10, 20]
>>> 