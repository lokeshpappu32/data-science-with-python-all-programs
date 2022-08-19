Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(11,22,33,44)
>>> help(t)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> 
>>> t.len()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.len()
AttributeError: 'tuple' object has no attribute 'len'
>>> len(t)
4
>>> x=list(t)
>>> x
[11, 22, 33, 44]
>>> type(x)
<class 'list'>
>>> x[3]=30
>>> t=tuple(x)
>>> x
[11, 22, 33, 30]
>>> t
(11, 22, 33, 30)
>>> t.index(33)
2
>>> t.index(44)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t.index(44)
ValueError: tuple.index(x): x not in tuple
>>> t[3]
30
>>> print(t[-1])
30
>>> t[1:3]
(22, 33)
>>> t1=(100,200,300,400)
>>> t+=t1
>>> t
(11, 22, 33, 30, 100, 200, 300, 400)
>>> t.remove(30)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t.remove(30)
AttributeError: 'tuple' object has no attribute 'remove'
>>> t.delete(30)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t.delete(30)
AttributeError: 'tuple' object has no attribute 'delete'
>>> t.update((500))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t.update((500))
AttributeError: 'tuple' object has no attribute 'update'
>>> t.update(500)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t.update(500)
AttributeError: 'tuple' object has no attribute 'update'
>>> t.update([10])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t.update([10])
AttributeError: 'tuple' object has no attribute 'update'
>>> t.append(111)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    t.append(111)
AttributeError: 'tuple' object has no attribute 'append'
>>> t.sort()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> l1={1,2,3}
>>> l2={3,4,5}
>>> l1.union(l2)
{1, 2, 3, 4, 5}
>>> l1.intersection(l2)
{3}
>>> l3={7,8,9}
>>> l1.intersection(l3)
set()
>>> l1.intersection_update(l2)
>>> l1
{3}
>>> l1.union_update(l2)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    l1.union_update(l2)
AttributeError: 'set' object has no attribute 'union_update'
>>> help(l1)
Help on set object:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
>>> l1.isdisjoint(l3)
True
>>> l1.issubset(l2)
True
>>> l1.superset(l2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l1.superset(l2)
AttributeError: 'set' object has no attribute 'superset'
>>> l1.issuperset(l2)
False
>>> l1.difference(l2)
set()
>>> l2.difference(l3)
{3, 4, 5}
>>> l1
{3}
>>> l2
{3, 4, 5}
>>> l3
{8, 9, 7}
>>> l2.difference(l1)
{4, 5}
>>> l2.difference_update(l1)
>>> l2
{4, 5}
>>> l2.discard(4)
>>> l2
{5}
>>> l1.symetric_difference(l3)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    l1.symetric_difference(l3)
AttributeError: 'set' object has no attribute 'symetric_difference'
>>> l1.symmetric_difference(l3)
{8, 9, 3, 7}
>>> l1={1,2,3,4,5}
>>> l2={3,4,6,7,8}
>>> l1.symmetric_difference(l2)
{1, 2, 5, 6, 7, 8}
>>> 
>>> l1.copy(l2)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    l1.copy(l2)
TypeError: copy() takes no arguments (1 given)
>>> l1.copy()
{1, 2, 3, 4, 5}
>>> s=int(input("Enter a number :"))
Enter a number :4
>>> s=int(input("Enter a number :"))