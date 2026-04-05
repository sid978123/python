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
print(sorted(L , reverse= True))
print(len(L))
print(min(L))
print(max(L))
'''Count '''

L = [ 1 , 2, 3 ,4 , 5,6]
L.count(5)
print(L.count(5))
