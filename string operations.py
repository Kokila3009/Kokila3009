Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1="kokila is is good girl"
>>> s1.replace("god","bad")
'kokila is is good girl'
>>> s1.replace("good","bad")
'kokila is is bad girl'
>>> s1.count("is")
2
>>> s1.find("bad")
-1
>>> s1.find("kokila")
0
>>> s1.find("is")
7
>>> s1.find("girl")
18
>>> s1.find("bad")
-1
>>> s1.find("girl"
	)
18
>>> s1.find("good")
13
>>> s1="kokila is ,is good,girl"
>>> s1.split(",")
['kokila is ', 'is good', 'girl']
>>> s1.upper()
'KOKILA IS ,IS GOOD,GIRL'
>>> s1.lower()
'kokila is ,is good,girl'
>>> len(s1)
23
>>> s1[-1]
'l'
>>> s1[0:6]
'kokila'
>>> 