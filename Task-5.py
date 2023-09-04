# Example of Basic operator in python:
#Arithmetic operator:
x = 10 
y = 8
print(x+y)
print(x-y)
print(x/y)
print(x*y)

#Example of Assignment operator
x,b =3,4 #we can assign value in 1 line
print(x,b)
x += y
print(x)

y -= x
print(y)

x *= y
print(x)

y /= x
print(y)

# Example of Logical and bitwise operator on boolean:
# logical operator:
a = True
b = False
print(a and b)# Using (and) logical operator

print(a or b)# Using (or) logical operator

print(not b)# Using (not) logical operator

print(not a)# Using (not) logical operator
# bitwise operator on boolean:
i =True
j =False

#Bitwise NOT
print(~i)

#Bitwise Shift
k=i<<5 #left shift
l=j>>5 #right shift
print(k,l)

#Any & all in python:
## Inplace and standard operator in python:
## Operator function in python|set 1;
## Inplace operator set|1:
## Logic gates in python:
## Python|a+=b is not always a a=a+b:
## Difference between == and is operator in python:
## Python membership and identity:
## Operator in,not in,is,is not: AND
print(i & j)

#Bitwise XOR
print(i ^ j)

#Bitwise OR
print(i | j)

#Example of Ternary operator:
m =2
n =10
print("yes" if m<n else "not")

#Example of Division operator in python:
display = n/m
print(display)

display = n//m #using floor division operator
print(display)

#Example of Operator overloading in python:
print(10+3) #Her by simple add operator function is perform
print(int.__add__(10,3)) #Overloads the + operator.

#Another example
class A:
    def __init__(self,x):
        self.x = x
    
    def __add__(self,other):
        return self.x + other.x
    
class B:
    def __init__(self,x):
        self.x = x
    
a=A(10)
b=B(20)
print(a+b)
# Example of Any & all in python:
#for All
number1 = [2,4,6,8]#cheking for all is even number or not
print(all([num1%2==0 for num1 in number1]))

number1 = [11,3,4,9]#cheking for all is odd number or not
print(all([num1%2==1 for num1 in number1]))

#for Any:
N =[22,33,44,55,66]#cheking for any is odd number or not
print(any([n%2==0 for n in N]))

N =[30,44,20,66]#cheking for any is even number or not
print(any([n%2==1 for n in N]))

# Example of Inplace and standard operator in python:
#standard operator
x = 3
y = 6
z = x + y  # Standard addition operation 

#Inplace operator
x = 5
y = 3
x += y  # Inplace addition operation


# Example of Operator function in python|set 1;
# Python code to demonstrate working of
# add(), sub(), mul()

# importing operator module
import operator
a = 4
b = 3

# using add() to add two numbers
print (operator.add(a, b))

# using sub() to subtract two numbers
print (operator.sub(a, b))

# using mul() to multiply two numbers
print (operator.mul(a, b))

# using div() to multiply two numbers
print (operator.truediv(a, b))
# Example of Inplace operator set|1:
x = operator.iadd(10,5)
print(x)

y = operator.imul(10,5)
print(y)

x = operator.ifloordiv(10,5)
print(x)

j = operator.iconcat('HELLO ','WORLD')
print(j)

# Example of Logic gates in python:
#AND GATE ex
def and_gate(x,y):
    return x and y
r = and_gate(1,1)
print(r)

def or_gate(x,y):
    return x or y
m = or_gate(0,0)
print(m)
# Example of Python|a+=b is not always a a=a+b:
a =[1,3,4,5]# original list
print(a)
print(id (a))

# BY using a=a+b:
b=[6,7] # adding new list in original
a =a+b
print(a)
print(id(a)) # id address is different

# By using a+=b:
a+=b
print(a)
print(id(a))# id address is same by using compound operator

# Example of Difference between == and is operator in python
# == checks for equality --->value equality
q = 10
r = 10
print(q+r)

# is checks for identity ---->refrence equality
s =4
t =s
print(s,t)

# Example of Operator in,not in,is,is not:
#Membership operator(in, not in)
# using (in)
cakes =["choclate cake","Vanilla Cake","Red Velvet Cake"]
print("choclate cake" in cakes) # True, because "choclate cake" is in the list 


# using (not in)
cakes =["choclate cake","Vanilla Cake","Red Velvet Cake"]
print("choclate cake" not in cakes) # True, because "choclate cake" is not in the list

#Identity operator(is, is not)
#Using (is)
n =3
j=n
print(n is j)
#Another example
l = [22,5,4,9]
k = [34,6,78]
print(l is k)
#Using (is not)
n =3
j=n
print(n is not j)

#Another example
l = [22,5,4,9]
k = [34,6,78]
print(l is not k)



