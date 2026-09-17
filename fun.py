#def greet(name):
 #   print("Hello",name)
#greet("Harshada")

#def sum(num1,num2):
 #   print(num1+num2)
#sum(12,23)

# def pi():
#     return 3.14
# pi=pi()
# print(pi)

# def add(a,b):
#     return a+b
# add=add(12,23)
# print(add)

#def name(name):
 #   print("hello",name)
#name()

# def num(n):
#     if n==0:
#        return 1
#     print(n)
#     num(n-1)
# num(10)

# def countdown(n):
#     if n==0:
#        return 1
#     print(n)
#     countdown(n-1)

def fact(n):
    if n==0:
       return 1
    return n*fact(n-1)
    
    
print(fact(5))
