'''Decomposition :'''
def is_even(num):

  '''This   function returns if a given number is odd or even 
  input - any valid integer
  output - odd/even
  created on - 09th april 2026'''
  if num % 2 == 0 :
    return 'even'
  else :
    return 'odd'



for i in range(1 , 11) :
  x = is_even(i)
  print(x) 
'''Arguments 
1. Default 
2. Positional argument
3. keyword argument :'''


def power(a=1 , b=1):
  return a**b

s = power(8 , 2)
print(s)
s = power(a=8 ,b=2) #Positional argument ; 
print(s)
s = power(b=8 , a=2) #keyword argument : 
print(s)


'''Args and kwargs'''

'''*args -> it allows us to pass a variable number of nonkeyword arguments to a function .'''

def multiply( a , b  , c) :
  return a*b*c


s = multiply(1 , 2, 3)
print(s)

def maltily(*args):
  product = 1 

  for i in args:
    product *= i

  return product

m = maltily(1 ,2 , 3, 4,7 ,5 , 6 ,1,2,3,3,4)
print(m)
print(is_even.__doc__)

'''kwargs'''
def display(**kwargs):
  for (key , value) in kwargs.items():
    print(key , value)


s=display(india="delhi",pak="islamabad",pakk='Lahore')



'''Global variable and Local variable : '''


'''Nested Functions : '''
def f():
  def g():
    print('inside function g')
    f()

  g()
  print('inside function f')


'''Functions as first class citizens : '''

def square(num) :
  return num**2


x = square(8)
print(x)

'''Returning a function : '''

def f() :
  def x ( a , b) :

    return a + b 
  return x 
val = f() (3 ,4)
print(val)


'''Benifits of a function  : 
1. code moduability 
2. code Reusability
3. code Readability'''


'''lambda Function :
a lambda function is a small
it is written in one line  '''

a = lambda x , y : x + y
print( a(2 , 3))

s = lambda s: 'a' in s
b = s('helloo')
print(b)



a = lambda x : 'even' if x%2 == 0 else 'odd'
s = a(6)
print(s)


'''Higher order function :'''


def transform(f , L ) :
  output = []
  for i in L :
    output.append(f(i))

  print(output)


L = [ 1 , 2 ,3 , 4, 5]
transform(lambda x :x**3 , L)




'''Map function  :'''
a = list(map(lambda x : x**2 , [ 1 ,2 ,3 , 4,5]))
print(a)


'''filter '''
L =  [ 1 ,2 , 3, 4 , 5]
a = list(filter(lambda x:x>3 , L))
print(a)




'''Reduce :'''

import functools
a = functools.reduce(lambda x , y : x+y , [ 1 , 2 ,3 , 4, 5])

print(a)

a = functools.reduce(lambda x , y :x if x>y else y , [ 11 , 22, 44 , 33 , 55 ])
print(a)

a =min([ 11 , 22, 44 , 33 , 55 ])
print(a)