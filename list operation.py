Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[2,"efg",9,True]
>>> l1{0}
SyntaxError: invalid syntax
>>> l1[1]
'efg'
>>> l1[1:4]
['efg', 9, True]
>>> l1[1]=100
>>> l1
[2, 100, 9, True]
>>> l1.append["hello"]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l1.append["hello"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l1.append["sparta"]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l1.append["sparta"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l1.append("hello")
>>> l1
[2, 100, 9, True, 'hello']
>>> l1.reverse()
>>> l1
['hello', True, 9, 100, 2]
>>> l1=[1,2,3,788,4,0,]
>>> l1.sort()
>>> l1
[0, 1, 2, 3, 4, 788]
>>> l1=["appale","dee","lion","tiger"]
>>> l1.sort()
>>> l1
['appale', 'dee', 'lion', 'tiger']
>>> l1.insert(0,"sparta")
>>> l1
['sparta', 'appale', 'dee', 'lion', 'tiger']
>>> l2=[1,2,3,4]
>>> l1+l2
['sparta', 'appale', 'dee', 'lion', 'tiger', 1, 2, 3, 4]
>>> l1
['sparta', 'appale', 'dee', 'lion', 'tiger']
>>> l1*3
['sparta', 'appale', 'dee', 'lion', 'tiger', 'sparta', 'appale', 'dee', 'lion', 'tiger', 'sparta', 'appale', 'dee', 'lion', 'tiger']
>>> 