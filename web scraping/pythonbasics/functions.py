
#simple function
def simple():
    print("my name is waleed iqbal")
simple() 

#single argument function
def arugumetfun(value1):
    print("my age is ",value1)

arugumetfun("23") 
arugumetfun("22") 
arugumetfun("21") 

#two argument function
def twoargu(value1,value2):
    print("my age is "+value1+ "\n and i am from "+ value2)
twoargu("23","faisalabad") 

#more arguments function
def moreargu(*value):
    print("my name is ",value[0])

moreargu("waleed iqbal","saad","huzaifa","ahmad")    

#loop simple function
def loop():
    
    fruits = ["apple","banana","orange"]
    for fruit in fruits:
        print(fruit)
loop()        
print("another loop\n")

loop()
print("another loop\n")

loop()

print("another loop\n")

#loop argument function
def loopargu(food):
    for fruit in food:
        print(fruit)

fruits = ["apple","banana","orange"]

loopargu(fruits)



#return function

def retu(x):
    return 5*x

y = input("enter the value ")
y = int(y)

result = retu(y)
print(result)