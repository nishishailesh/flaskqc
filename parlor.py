#!/usr/bin/python3
import time
def decorator_functionn(original_function):
    def wrapper(a,b):
        print('Executed Before second')
        result = original_function(a,b)
        print('Executed After second')
        return result
    return wrapper

############decorator created and called##########
############function created, and given name display_info()#######
####display_info() is called########

@decorator_functionn
def display_info(name, age):
    print('arguments provided are ({}, {})'.format(name, age))

display_info('Mr Bean', 66)
print(display_info.__name__)

##############non decorator syntax created and called##########
############function created, but no name function defination is returned#######
####defination stored as display_infoo and called########

def display_infoo(name, age):
    print('display_info nn ran with arguments ({}, {})'.format(name, age))
display_infoo=decorator_functionn(display_infoo)
#Thus, @ syntax is a short for of above 3 lines of code

display_infoo('h',200)
print(display_infoo.__name__)


def decorators(*args, **kwargs):
    for item in args:
        if(type(item)=='str'):
            print("arg:"+item)
    for item in kwargs:
        if(type(kwargs[item])=='str'):
            print(item+":"+kwargs[item])
            
    #following just return a function
    #duty of this function is to return ANOTHER_FUNCTION passed as parameter
    def yyy(xxx):
        return xxx
    return yyy
 
@decorators("a","b",one="ONE",two="TWO")
def func():
    print("ugly")
    pass

func()

@decorators()
def func2():
    print("ugly")
    pass
func2()

'''
#produce errors
@decorators
def func3():
    print("ugly")
    pass
func3()
'''

def func4():
    print("directly ugly")

    
#xxx=decorators(func4)
#xxx()

#decorators return a function(yyy) which take a function(xxx) as parameter.
#This yyy returns the function xxx
#so abc is just func4
abc=decorators("a","b",one="ONE",two="TWO")(func4)
abc()

#so this is valid
decorators("a","b",one="ONE",two="TWO")(func4)()
