'''Tuple , set and Dictionaryy'''

'''A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
Ordered 
unchangeable
allow duplicate value'''

#Creation of tuple . 
# t1 = ()
# print(t1)

# t2 = (2 ,)
# print(t2)
# print(type(t2))

# t4  = (1 , 2, 3, 4, "hello" , True , (1 , 2,3 ))

# t5 = tuple("hello")
# print(t5)

# '''How to access item in the tuple :'''

# print(t4[-1])
# print(t4[0 : 4 : -1 ])


'''Deletion in the tuple'''
# t3 = ( 1 , 2, 3, 4, 5, 5)
# del t3 # here we can not delete any specific part of the tuple because we can not edit any tuple , but we can delete whole tuple 
# print(t3)

'''Opereation In Tuple :'''

# + and *
# t1 = ( 1 ,2,3,4)
# t2 = ( 5 , 6, 7, 8)

# print(t1 + t2)
# print(t1 * 3)

# '''Membership : '''
# print(1 not in t1 )

# '''Iteration : '''
# for i in t1 :
#   print(i)


'''Functions :'''
# t1 = ( 1 ,2,3,4)
# print(len(t1))
# print(sum(t1))
# print(min(t1))
# print(max(t1))
# print(sorted(t1 , reverse=True))

# '''Count'''
# t1 = ( 1 ,2,3,4)
# print(t1.count(2))

# '''index :'''

# t1 = ( 1 ,2,3,4)
# print(t1.index(3))

# '''tuple unpacking :'''
# a ,b , c , *others = ( 1 , 2, 4 , 2 ,3 ,3)
# print(a , b, c)
# print(others)

# a = 1 
# b = 3
# a , b = b , a 
# print(a ,)

'''Zip'''
# a = ( 1 ,2,3,4)
# b = ( 5 , 6, 7, 8)

# print(list(zip(a , b)))
# print(tuple(zip(a , b)))

# '''Any Immutable data type  is faster than mutable'''
# l = [i + j for i , j in zip(a , b)]
# print(l)



'''A set is unordered Collection of items . Every set element is Unique
'''
'''Creation of set :'''

# s = set()
# print(type(s))

# s = { 1, 2, 3 , 4}
# print(s)

# s = { 1, 2, 4.5,"hello" , 4} # python TRUE ko 1 consider karta hai
# print(s)

# s = { 1, 2, 3 , 4}
# print(list(s))
# print(set([1, 2, 3, 5, 6]))

# s1 = { 1 , 2, 3, [ 1 ,2,4 ]} # it will give an error because we can not enter mutable items inside the set  , so it will give an error: 



# s1 = { 1 ,2 , 3}
# s2 = { 1 ,2 , 3}
# print(s1 == s2)

# '''Acccessing Items in the set : '''
# s1 = { 1 ,2 , 3}

#Editing is not allowed in the set : but we can add  new items and delete items :
# print(s1.add(9 )) # add only one item in the list ; 
# print(s1.update([ 5 , 6, 7 , "hello"])) # it can add multiple item in the set 
# print(s1)

'''Deletion item in the set ; '''
# s1 = { 1 ,2 , 4 , 5, 3}
''''''
# del s1 
# print(s1)
'''Discard'''
# print(s1.discard(5))
# print(s1)
# '''Remove '''
# s.remove(49)
# print(s)

'''NOTE ->  discard never through an error but Remove through an error : '''

'''Pop  -> it randomly delete the item in the set : '''
# s1.pop()
# print(s1)

'''Clear -> it delete whole itemm in the set : '''
# s1.clear()
# print(s1)

'''NOTE ->> OPERATION ON SET : '''
'''UNION  of set :'''
# s1 = { 1 ,2 , 4 , 5, 3}
# s2 = { 6 , 7, 8,9, 10 , 11}
# print(s1|s2)

# '''Intersection of the set : '''
# s1 = { 1 ,2 , 4 , 5, 3}
# s2 = { 6 , 7, 8,9, 10 , 11}
# print(s1 & s2)

# '''Difference : '''
# s1 = { 1 ,2 , 4 , 5, 3}
# s2 = { 6 , 7, 8,9, 10 , 11}
# print(s1 - s2)

# '''Symmetric Operation : '''
# s1 = { 1 ,2 , 4 , 5, 3}
# s2 = { 6 , 7, 8,9, 10 , 11}
# print(s1 ^ s2)


s1 = { 1 ,2 , 4 , 5, 3}
for i in s1 :
  print(i)


''' NOTE ->  function in set 
'''
s = { 1 ,2 , 4 , 5, 3}

len(s)
sum(s)
min(s)
max(s)
sorted(s , reverse=True)

s1 = { 1 ,2 , 4 , 5, 3}
s2 = { 9 , 8, 7, 6, 5,4}

u = s1.union(s2)
print(u)

s1 = { 1 ,2 , 4 , 5, 3}
s2 = { 9 , 8, 7, 6, 5,4}

'''Intersection and Intersection_update'''

s1.intersection(s2)
s1.intersection_update(s2) #it stores intersection value in the s1 and update it permanentlyy ; 

print(s1)
print(s2)

'''difference and difference_update'''

s1 = { 1 ,2 , 4 , 5, 3}
s2 = { 9 , 8, 7, 6, 5,4}

s1.difference(s2)
s1.difference_update(s2)
print(s1)
print(s2)

'''Symmetric_differnece and Symmetric_difference_update :'''

s1 = { 1 ,2 , 4 , 5, 3}
s2 = { 9 , 8, 7, 6, 5,4}

s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(s1)
print(s2)


'''Isdisjoint and issubset  , issuperset'''

s1 = { 1 ,2 , 4 , 5, 3}
s2 = { 9 , 8, 7, 6}

d = s1.isdisjoint(s2)
print(d)

s = s1.issubset(s2)
print(s)

s = s1.issubset(s2)
print(s)

'''Copy'''
s1 = { 1 ,2 , 4 , 5, 3}
s2 = s1.copy()
print(s2)



'''**************************'''
'''FROZEN SET -> this set is Immutable so we can not edit this set : '''

'''Here 2D frozen set are possible : '''
fs = frozenset([ 1, 2, 3, 5]) 
fs = frozenset([ 1, 2, "hello", 5]) 
print(fs)

fs = frozenset([ 1 , 2 , frozenset([ 1 , 2, 3])])
print(fs)

'''Set Comprehension : '''
s = { i**2 for i in range(1 , 12) if i>5}
print(s)

'''NOTE -> DICTIONARY '''

'''it is a collection of key and pairs 
1. Mutable 
2. Indexing has no meaning
3. keys can not be duplicate :
4. Keys can not be mutable "'''

'''Creation '''
d = {}
d = {"name" : "sid " , "age " : 12}
print(d)
d1 = {(1 ,2, 3):12 , "hello" : "world"}
print(d1)

s = {
  'name' : 'nitish',
  'college' : 'bit',
  'sem' : 4,
  'subject ' : {
    'dsa' : 32,
    'math' : 32,
    'eng' : 34
  }
  
}

d4 = dict([(1 ,2 ) , ( 2 , 3)])
print(d4)

'''mutable items as keys not allowed : '''

# d6 = { 'neme' :"sid"  , [1 ,2 , 4 ] : 1} # error , because we can not add mutable element so it is not allowed 

'''Fetching items from the dictionary : '''
my_dict = {"name " : "sid " , " age " :21}
my_dict[' age ']
my_dict.get("age")

'''Adding key-value pair : '''
d4['gender'] = 'male'
print(d4)

'''Removing key-value pair : '''
# 1 .pop

d = {"name " : "sid " , " age " :21}
# d.pop("age")
# print(d)

'''POP ITEM '''
d.popitem() # delete item from the last 
print(d)

'''del '''
d = {"name" : "sid" , "age" :21}
del d["name"]
print(d)


d.clear() # elear all dictionaay : 
print(d)

'''Editing key-value pair : '''
s = {
  'name' : 'nitish',
  'college' : 'bit',
  'sem' : 4,
  'subject ' : {
    'dsa' : 32,
    'math' : 32,
    'eng' : 34
  }
  
}

print(s['subject ']['dsa'])
s['subject ']['dsa'] = 34
print(s)

s['subject ']['ds'] = 38 # adding new item in the list :
print(s)

'''deletion in the dictionaty : '''
del s['subject ']['dsa'] 
print(s)

'''edithing in the dictionary ; '''
s['subject ']['dsa'] = 34
print(s)

'''NOTE -> Dictionary Operations : 
1. Membership 
'''

print('name' in s )
'''2. Iteration'''

d = {'name' : "nithish" , "gender " : "Male"}

for i in d :
  print(i , d[i])



'''len'''
d = {'name' : "nithish" , "gender " : "Male"}

len(d)
print(d)
sorted(d , reverse=True)

'''NOTE => items , keys and pairs '''

d = {'name' : "nithish" , "gender " : "Male"}

print(d.items())
print(d.keys())
print(d.values())

'''update  '''
d1 = { 1:2 , 3: 4 , 5:9}
d2 = {4:9 , 5:10}
d1.update(d2)
print(d1)


'''Dictionary Comprehension :'''

'''print 1st 10 numbers and their squares :'''

s = { i:i**2 for i in range(1 , 11)}
print(s)

distance = {'delhi':1000,'mumbai':2000,'banglore':3000}

s = {key:value*0.62 for (key , value) in distance.items()}
print(s)


days = {'sunday' , 'monday' , 'tuesday' , 'wednessay' , 'thursday ' , 'friday' , 'saturday '}
temp_c = {30.5 , 32 , 34 , 45 ,32, 345 ,45,54}

s = {i:j for ( i , j) in zip(days , temp_c)}
print(s)


product = {'phone':10  , 'laptop ' : 0 , 'charger':32 , 'tablet':0}
s = { i:j for (i , j) in product.items() if j  > 0}
print(s)


'''print table of number from 2 to 4'''

s = {i:{j*i for j in range(1 , 11)} for i in range(2 , 4)}
print(s , end="")
