#demonstration using for if while
x=int(input("enter x"))
y=int(input("enter y" ))
print("select the opertion required")
print("MENU")
print("1.string concatination"
      "2.string replication"
      "3.addition"
      "4.substrction"
      "5.string length"
      "6.MULTIPLICATION TABLE"
      "7.DIVISON")
c =int(input("enter your choice"))

if c==1:
       print(x+y) 
       print("MENU")
       print("1.string concatination"
      "2.string replication"
      "3.addition"
      "4.substrction"
      "5.string length"
      "6.MULTIPLICATION TABLE"
      "7.DIVISON")
       c =int(input("enter your choice"))
if c==2:
        print(x * 3,"and",y*3)
        print("MENU")
        print("1.string concatination"
          "2.string replication"
          "3.addition"
          "4.substrction"
          "5.string length"
          "6.MULTIPLICATION TABLE"
          "7.DIVISON")
        c =int(input("enter your choice"))
if c==3:
        print(x+y)
        print("MENU")
        print("1.string concatination"
          "2.string replication"
          "3.addition"
          "4.substrction"
          "5.string length"
          "6.MULTIPLICATION TABLE"
          "7.DIVISON")
        c =int(input("enter your choice"))
if c==4:
        print(y-x)
if c==5:
        print ("lenth of the string is",len(x))
if c==6:
        for i in range(1,21):
            print(int(x),"x",i,"=",int(i*x))
if c==7:
        print(x,"/",y,"is",x//y)
if c>7 and c<=0:
        print("enter valid key")
            
            
