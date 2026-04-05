

'''we have to print n/n!'''


# n = int(input("Enter a number: "))
# f1 = 1
# sum = 0
# for i in range(1 , n+1) :
#   f1 = i*f1
#   sum += i/f1
# print("The factorial is : " ,f1)  
# print("the sum of i/(f1!)  is : " , sum)


'''here we have to print the pattern '''
# n = int(input("Enter the number :"))

# for i in range( 1 , n+1):
#   for j in range(1 , i+1):
#     print("*" , end = '')
#   print()
   
# n = int(input("Enter the number :"))

# for i in range( 1 , n+1):
#   for j in range(1 , i+1):
#     print(j , end = '')

#   for j in range(i-1, 0, -1):
#     print(j , end = '')
  
#   print()

'''Loop controll Statement :'''
#Negative Indexing : it goes from right to left
s = "hell  world" 
print(s[-3])

#Slicing in String : 
# s = "hello world :"
# print(s[6:0:-1])
# print(s[::-1])
# print(s[-5:-1])
# print(s[-1:-6])

'''python strings are immutable :'''
s = "hello world"


#Operations in Strings 

"mumbai" > "delhi"
'delhi' > 'Delhi'


for i in 'hello' :
  print(i)

'd' in 'delhi'


'''Here we are going to learn about functions in python :'''
len('hello world ')
max("hello world")
min("hello world")
sorted("hello world")
sorted("Hllo Myseld " , reverse=True)

s = ' hello world'
s.capitalize()
s.title()
s.upper()
s.lower()
'hello world'.swapcase()


'''Count , find and index'''
"my name is sidd ".count(i)
"my name iis utimue".find("is")


m = 'my name sis '.endswith('sis')
print(m)

name = 'sid'
age = 21
print("my name is {} and age is {}".format(name , age))



"sid123".isalnum()
'sid1231'.isalpha()
'sid123'.isdigit()
'sid12345'.isidentifier()

'first_nmae'.isidentifier()


print('siddharth is just a man who is living in this frazile world'.split())
print("uknowme is you are".split('no'))
print("".join(["my name is u know me"]))


print('hey u are pretty'.replace('u','is'))

print('dan is dying in the username        ee      '.strip())