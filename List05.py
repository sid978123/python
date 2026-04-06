'''here we are going to learn about list here '''

'''List act like dynamic array in which u can store multiple items of same type or different :


List are mutable
list are Ordered '
list are hetrogeneous 
it can have duplicate value 
it can be nested 
can contain any kind object in python

 '''
#1D list 
print([ 1 , 2 ,3 ,4 ,5])

#2D list 
[ 1 , 2 ,3 ,4 ,[1 , 2 ,3 ]]

#3D list 
[ 1 , 23 , [ 2 , 12 , [ 1  , 3, 4, 5,5]]]



'''fetch item from the list :'''
'''Positive indexing  , it means it goes from left to right and start with 0 '''
L = [ 1 , 2 ,3 ,4 ,5]
print(L[0])  

L = [ 1 , 2 ,3 ,[4 ,5]]
print(L[3][1])

'''Negative indexing , it start form right to left and start with -1'''

L = [ 1 , 2 ,3 ,[4 ,5]]
print(L[-1][-2])


L = [ 1 , 23 , [ 2 , 12 , [ 1  , 3, 9, 5,5]]]

print(L[2][2][2])
print(L[-1][-1][-3])


'''Slicing in the list :'''
L = [ 1 ,2 ,3 , 4 , 5 ,6,7,8,9]
print(L[0::2])
print(L[::-1])

'''Add the item in the list :'''
'''APPEND -> it always add only one item in the list '''

# L = [ 1 ,2 ,3 , 4 , 5 ,6,7,8,9]
# L.append(10)
# print(L)
'''extend : it always add more than one item in the list '''
L = [ 1,2,3,4,5]
L.extend([ 6,7,8,9])
L.extend("delhi")
# L.append([ 6,7,8,9])
print(L)


'''Insert in the list'''
L = [ 1 , 2, 3, 4,5]
L.insert(1 , 29)
print(L)

'''How to edit any existing Items in the list :'''

L = [ 1 , 2, 3, 4,5]
L[-1] = 200
print(L)
L[1:4] = [ 233 , 4,44,4,5,]
print(L)


'''Deletion in the list  : '''

L = [ 1 , 2, 3 ,4 , 5,6]
del L[-1:-4:-1]
print(L)

'''Remove in the list :'''

L = [ 1 , 2, 3 ,4 , 5,6]
L.remove(5)
print(L)


'''Pop in the List :'''

L = [ 1 , 2, 3 ,4 , 5,6]
L.pop() # default it delete from the last if we do not priovide any index 
L.pop(0)# It delete "1 " in the list : # default it delete from the last if we do not priovide any index 
print(L)


'''Operator in the list :'''
'''Only two operation works in the list
Arithmetic( + . *)
Membership
Loop
'''
'''Merge two list using + operator : '''
L = [ 1 , 2, 3 ,4 , 5,6]
print(L*3)

'''Membership Opererator : 
in 
not in '''


L = [ 1 , 2, 3 ,4 , 5,6]
L1 = [ 1 , 2, 3 ,4 , [5,6]]
print( 5 not in  L)
print( [5 , 6] in L1)

'''Loop in list : '''

L = [ 1 , 2, 3 ,4 , 5,6]
L1 = [ 1 , 2, 3 ,4 , [5,6]]
L2 = [ 1 , 23 , [ 2 , 12 , [ 1  , 3, 9, 5,5]]]
for i in L2 :
  print(i)

'''Some functions in the list  :
len/min/max/sorted'''

L = [ 1 , 2, 3 ,4 , 5,6]
print(sorted(L , reverse= True)) #Sorted temperary short the list
print(len(L))
print(min(L))
print(max(L))
'''Count '''

L = [ 1 , 2, 3 ,4 , 5,6]
L.count(5)
print(L.count(5))

'''Index '''
L = [ 1 , 2, 3 ,4 , 5,6]
L.index(1)

'''Reverse '''
L = [ 1 , 2, 3 ,4 , 5,6]
L.reverse() # It reverse the string permanent and it does not create any new list :
print(L)


'''Sort in List '''
L = [ 1 , 4 ,3 , 8, 5,6,7]

L.sort()
print(L)

'''Coppyy in List'''

L = [ 1 , 2, 3 ,4 , 5,6]
L1 = L.copy()
print(L1)

'''List Comprehension : '''

#newList = [ expression for item in iterable if condition == True]
''' Add 1 to 10 numbers to a list : '''
L =  [ [ i for i in range(1 , 11)]]
print(L)

'''Scalar multiplication on a vector :'''

v = [ 2 , 3, 4]
s = -3
L = [ s*i for i in v]
print(L)

'''Add squars  :'''
v = [ 2 , 3, 4]
L = [ i**2 for i in v]
print(L)

'''print all the numbers dividible y 5 in the range of the 1 to 51'''

L = [ i for i in range(1 , 51) if i % 5 == 0 ]
print(L)
'''find the language which start with letter p'''
languages = [ 'java' , 'python ' , 'php' , 'c ', 'javascript']
L = [ language for language in languages if language.startswith('p')]
print(L)

'''Nested if   with List comprehension : '''

basket = [ 'apple', 'guava' , 'cherry ' , 'banana']
my_fruits  = ['apple' , 'kiwi' , 'grapes '  , 'banana']

L = [fruit for fruit in my_fruits if fruit in basket  if fruit.startswith("a")]
print(L)


'''Print the (3*3) matrix ;'''
L = [[i*j for i in range(1 ,4)] for j in range( 1 , 4) ]
print(L , end= " ")

'''Cartesian product -> List comprehension on 2 list together :'''



L1  = [1 , 2, 3, 4 ]
L2  = [5 , 6, 7, 8 ]
L = [ i*j for i in L1  for  j in L2]
print(L)

'''2 ways to taversal a list : '''
  # item Wise 
L  = [1 , 2, 3, 4 ]

for i in range(0 , len(L)):
  print(L[i] , end= " ")

'''Zip function : '''

L1  = [1 , 2, 3, 4 ]
L2  = [5 , 6, 7, 8 ]
L = list(zip(L1 , L2))
L3 = [i+j for i , j in zip(L1 , L2)] 
print(L3)


''' we can store a built in function in the list  '''
L = [ 1 , 2 , print , type , input]
print(L)

