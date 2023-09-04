# Task-5
## operator:
We can say that an operator is a symbol that tells the compiler to perform specific mathematical, conditional, or logical functions.

Python divides the operators in the following groups:

Arithmetic operators,
Assignment operators,
Comparison operators,
Logical operators,
Identity operators,
Membership operators,
Bitwise operators.
## Basic operator in python:
Arithmetic operator(+,-,/,*)is the basic operator in python.

Assignment operator is(=.+=,-=,/=,%=,//=,**=,&=,|=,^,<<=,>>=).
## Logical and bitwise operator on boolean:
### Logical operator:
Logical AND: True if both the operands are true	

Logical OR: True if either of the operands is true 

Logical NOT: True if the operand is false 
## Bitwise operator:
Bitwise AND (&):

Bitwise OR (|):

Bitwise NOT (~):

Bitwise XOR (^):

Bitwise left shift (<<):

Bitwise right shift (>>):

Above us bit wise operator we can use this operation with boolean (True,false).
## Ternary operator:
It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.

Syntax :  [on_true] if [expression] else [on_false] 
## Division operator in python:
In Python, the division operator (/) is used to perform division between two numbers, and it returns a floating-point result.by using floor division (//) it gives the intiger result.
## Operator overloading in python:
Operator + is used to add two integers as well as join two strings and merge two lists.You might notice that same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 
## Any & all in python:
Any and All are two built-in functions provided in python used for successive And/Or.
### Any:
 Any Returns true if any of the items is True. It returns False if empty or all are false.
### All:
All Returns true if all of the items are True (or if the iterable is empty).It returns False if
 all are false.
## Inplace and standard operator in python:
### Inplace operator:
Inplace operators behave similarly to normal operators except that they act in a different manner in case of mutable and Immutable targets.
### Standard operator
Standard operator/Normal operator’s “add()” method, implements “a+b” and stores the result in the mentioned variable.
## Operator function in python|set 1;
Python has predefined functions for many mathematical, logical, relational, bitwise etc operations under the module “operator”. Some of the basic functions are:

1. sub(a, b)
2. add(a, b)
3. mul(a, b)
4. div(a, b)
5. ne(a, b)
6. pow(a, b)
7. ge(a, b)
8. gt(a, b)
9. mod(a, b)

## Inplace operator set|1:
Python in its definition provides methods to perform inplace operations, i.e doing assignment and computation in a single statement using “operator” module. For example,

x += y is equivalent to x = operator.iadd(x, y)
## Logic gates in python:
Logic gates It takes one or two inputs and produces output based on those inputs. Outputs may be high (1) or low (0). 

There are seven basic logic gates are: AND gate, OR gate, NOT gate, NAND gate, NOR gate, XOR gate, an XNOR gate.
## Python|a+=b is not always a a=a+b:
Reason:

Normal operation a=a+b:

behaind the secene is perform by this a=a+[3]:-Uses __add__

Compound operation a+=b:

behaind the secene is perform by this a+=[3]:-Uses __iadd__
## Difference between == and is operator in python:
#### == compares the values of objects.

It checks whether the contents of the objects are the same, regardless of whether they are the same object in memory.

It returns True if the values are equal and False if they are not.
#### is compares the identities (memory addresses) of objects.

It checks whether two variables refer to the same object in memory.

It returns True if the objects are the same (i.e., they have the same memory address) and False if they are not.
## Python membership and identity:
### Membership:
It is used to test wether the value is the member of sequence or collection.

Python provides two membership operators:
#### ‘in’ and ‘not in’.
### Identity:
Identity operators in Python are used to compare the identity of two objects.

 In Python, there are two identity operators:
 #### “is” and “is not.