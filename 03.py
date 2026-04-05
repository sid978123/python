# m = input("Enter your name : ")
# count = 0
# for i in m :
#   count += 1

# print(count)


'''Extract username from a given email :
if the email is nitishkumar@gmail.com 
username = nitishkumar
'''

# s = input("Enter the email :")
# if "@" not in s :
#   print("invalid Email : Please Enter correct email : Error")
# else :
#   position = (s.find("@"))
#   username = s[0:position]
#   print(username)

''' Count the frequency of the particular character in a provided strings :'''

# s = input("Enter the string :")
# var = input("Enter the character :")
# count = 0
# for i in s :
#   if i == var :
#     count += 1 
# print(count)    

'''Wap which can remove a particular character form a string :'''

# s = input("Enter the string :")
# var = input("Enter the character what u wish to remove :")

# result = ""

# for i in s :
#   if i == var :
#     continue
#   else :
#     print(i , end = "")

'''check wheather the given string is palindrome or not :'''



# for i in s[::1][:len(s)//2]:
#   for j in s[::-1][:len(s)//2]:
#     if i != j :
#       print("Error")
#       break
      
#     else :
      
#      print("String is palindrome :") 
# s = input("Enter the string :")  
# flag = True
# for i in range(len(s)//2) :

#   if s[i] != s[-(i+1)] :
#     flag = False
#     break
  

# if flag :
#   print("String is palindrome :")

# else :
#   print("Error :")      

'''write a program to count the number of words in a string without split()'''


# s = input("Enter the string :")
# temp = ''
# L = []
# count = 0
# for i in s :
#   if i != ' ' :
#     temp += i
    
#   else :
#     L.append(temp)
#     count += 1
#     temp =''
# L.append(temp)    
# print(L) 
# print(count ) 

''' wap to convert a string to title case without using the title() :'''

# s = input("Enter the string :")
# for i in s.split() :
#   m = (i[0].upper()+i[1::].lower())
#   print(m)


'''wap that can convert an integer to string :'''

# s = int(input("Enter the Integer value:"))
# strr = str(s)
# print(type(strr) , strr) 
  










''''Order of growth'''

'''given integer to string '''

# s = int(input("enter the number :"))
# digit = '0123456789'
# result = ""
# while s != 0 :
#   result = digit[s%10] + result
#   s = s // 10
# print(s)


# L = [ 1, 2, 3, 4]



'''Print  the following pattern . write a program to use for loop to print the following reverse number patterns'''


# n = int(input("Enter the number :"))

# for i in range(1 , n+1):
#   for j in range(n , 0 , -1):
#     print(j ,end=" ")
#   n-=1  
#   print()



'''Print the following patterns '''

# n = int(input("Enter the number :"))

# for i in range(1 , n+2):
#   for j in range(i):
#     print(" * ", end= " ")
#   print()
# for i in range(1 , n+1):
#   for j in range(n , 0 , -1):
#     print(" * ", end= " ")
#   n-=1  
#   print()


'''wap  to print the folllowing patterns :'''

# n = int(input("Enter the number :"))

# for i in range(1 , n+1):
#   print(" "*(n-i) , end= " ")
 
#   for j in range(2*i-1):
#     print("*" , end= " ")

#   print()


'''write a program to print the following patterns '''

# n = int(input("Enter the number :"))

# for i in range(1 , n+1) :
#   for j in range(i , 0 , -1):
#     print(j , end= " ")

#   print()


'''wap to  find the sum of the series til the nth term'''
'''1 + x^2 / 2 + x^3 / 3 + .... x^n / n'''

# n = int(input("Enter the number n : "))
# x = int(input("Enter the value of X :"))
# sum = 0
# for i in range(1 , n+1) :
#   sum += (x**i)/i
# print( 1 + sum)

'''the natural logarithm can be aproximated by the following series :'''

# 
# x  = int(input("Enter the value of X :"))
# total =  0
# for i in range(1 , n+1) :
#   total += (1/2)*((x-1)/x)**i
# print(total)

'''wap to calculate the sum of series up to n term. for example if n = s the series becomes 2 + 22 +222 + 22222 + 22222  = 24690 . Take the user input and then calculate . And the output style should match which give in the example :'''

# n = int(input("Enter the number n : "))
# total = 0
# for i in range( 1 , n+1) :
#   s = "2"*i
#   # print(s)
#   total += int(s)
  
# print(total)


'''wap to print all the unique combinations of 1 , 2 , 3, 4'''

# n = int(input("Enter the number n : "))
# L = []
# for i in range(1 , n+1):
#   for j in range(1 , n+1):
#    L.append(j)
#   print(L , end= " ")
#   # L = []
#   print()


#   for i in range(len(L)):
#      if L[i] == L[i-1] :
#        print("error")
#      else :
#        s = "successfulll"
    
#   print(s)


# from itertools import permutations

# n = int(input("Enter n: "))

# nums = list(range(1, n + 1))

# for p in permutations(nums):
#     print(*p)
  
    
 
'''wap that will take a decimal number as input and print out equivalent of the number :'''

# n = int(input("Enter the Decimal number n : "))
# # m=[]
# # n=[]
# for i in range(1 ,int( n/2)):
#   if(n / 2 == 0) :
#    print("0")
  
#    continue
#   elif ( n / 2 != 0 ):
#     print("1")
#     continue


'''check wheather the string is symmetrical or not '''



# s = input("Enter the string :")

# mid = len(s)//2 

# if len(s) % 2 == 0 :
#   first = s[:mid]
#   last = s[mid :]
# else :
#   first = s[:mid]
#   last = s[mid + 1 :]

# if first == last :
#   print("String are Symmetrical :")
# else :
#   print("String are not syymetrical : ")


'''Create short form from initial character : '''


# s = input("Enter the string :").split()
# print(s) 
# short = " "
# for i in range(len(s)):
#   short += s[i][0].upper()
# print(short)  


'''Append second string in the middle of first string :'''


# s1 = input("Enter 1st string :")
# s2 = input("Enter 2nd string :")
# n = len(s1)//2
# last_half = ""
# first_half = ""
# for i in range(n) :
#   first_half  += s1[i]
 
# for j in range(n , len(s1)) :
#   last_half  += s1[j]

# print(last_half)
# middle = first_half + s2
# final = middle + last_half
# print(final)



'''Given string contains a combination of the lower and uppercase letter > Write a program to arrange the character of a string so that all lower case letters should come first :'''

# s = input("Enter the mixed String : ")

# upper = ""
# lower = ""
# for ch in s :
#   if ch.isupper():
#     upper += ch

#   elif ch.islower():
#     lower += ch
# final = lower + upper 
# print(final)

'''Take alphanumeric string input and print the sum and average of the digits that appears in the string , ignoring all other characters : '''


# s = input("Enter the alphnumeric String : ")
# total = 0
# count = 0
# for ch in s :
#   if ch.isdigit() :
#     total += int(ch)
#     count += 1

# avg = total / count
# print("the total sum is : " , total)
# print("The average is : " , avg)

'''Remove all the character form a strig except integers '''

# s = input("Enter the alphnumeric String : ")
# total = []
# count = 0
# for ch in s :
#   if ch.isdigit() :
#     total.append(int(ch))
#     count += 1

# print(total)


'''Reverse words in a given string :'''

# s = input("Enter the alphnumeric String : ").split()

# final = s[::-1]
# print(" " .join(final))


'''find uncommon words from two strings :'''

# s1 = input("Enter the String : ").split()
# s2 = input("Enter the  String : ").split()

# uncommon  = []
# for word in s1 :
#   if word not in s2 :
#     uncommon.append(word)

  
# for word in s2 :
#   if word not in s1 :
#     uncommon.append(word)

  
# print("Uncommon words are :" , uncommon)
  

'''find the location of the word in given string :'''

# s = input("Enter the string :").split()
# word = input("Enter the word whose location you want :")

# for ch in range(len( s )):
#   if s[ch] == word :
#     print("index is :", ch , "  " ,"value is : " , s[ch])


'''write program that can delete all the duplicate character from a string . User will provide the input'''


s = input("Enter the string :")
# result = ""
# for ch in s:
#   if ch not in result :
#     result += ch


# print(result)  

result = ""
for i in range(len(s)):
  duplicate = False
  for j in range(i):
    if s[i] == s[j]:
      duplicate = True
      break
  if not duplicate :
    result += s[i]  
  
print(result)


