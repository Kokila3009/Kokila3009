import sys
def add():
    n1=int(input("enter a"))
    n2=int(input("enter b"))
    
    r=n1+n2
    print("sum is",r)

def sub():
        n1=int(input("enter a"))
        n2=int(input("enter b"))

        if n1>n2:
            r=n1-n2
            return(r)
            
        else:
            r=n2-n1
            return(r)
            

def mul_table(a):
    for i in range(1,11):
        print(a,"x",i,"=",i*a)

def prime(n):
    prime=False
    if n==0 or n<0:
        sys.exit("invalid input")
    else:
        for i in range(2,n):
            if n%i==0:
              prime=True
               break
        
        if prime:
            print(n,"is not a prime") 
        else:
            print(n,"is a prime")
def factorial(a):
    fact=1 
    for i in range(1,a+1):
        fact=fact*i
    print("the factorial of",a,"is",fact)
while(1):       
    print("\nMENU\n \n1.ADDITION\n2.SUBSTRCTION\n3.MULTIPLICATION TABLE\n4.TO CHECK PRIME\n5.TO GET FACTORIAL\n")        
    choice=(int(input("enter your choice")))
    if choice==1:
        r=add()
    elif choice==2:
         r=sub()
         print("on substraction",r)
    elif (choice==3):
        m=int(input("enter a number"))
        mul_table(m)
    elif(choice==4):
        n=int(input("enter a number"))
        r=prime(n)
    elif(choice==5):
        y= int(input("enter a number"))
        factorial(y)
    else:
        print("enter valid operation key")
        break
    
