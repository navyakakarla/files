#function defination
def fun():#function definiation
    print("this function")#function body
fun()#function call
#calling parameters to function
def fun(a,b,c):
    print("this is function",a,b,c)
fun(1,2,3)
#key word arguments
#for single parameter for multiple arguments
def fun(*a):
    print("this is a function",a)
fun(1,2,3)   
#data  like dictionary
def fun(**a):
    print("this is a function",a)
fun(a=1,b=2)
#nested functions
def outer():
    print("outer")
    def inner():
         print("inner")
    inner()
outer()
#import 
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)