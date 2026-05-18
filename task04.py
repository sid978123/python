# '''combine two list index wise'''

# list1 = ['M', 'na', 'i', 'Kh']
# list2 = ['y', 'me', 's', 'an']

# L = []

# for i in range(len(list1)):
#     L.append([list1[i], list2[i]])

# print(L)

# '''add new item to list after a specific item '''

# L1 = [10 , 20 , [300 , 400 , [ 5000 , 6000] , 500] , 30 , 40]
# L1[2][2].append(7000)
# print(L1)


# '''write a program to show no of items of each candy type'''

# candy_list = ['Jelly Belly', 'Kit Kat', 'Double Bubble', 'Milky Way', 'Three Musketeers']
# no_of_items = [10, 20, 34, 74, 32]
# L = []
# for i in range(len(candy_list)):
#     L.append([candy_list[i] , no_of_items[i]])

# print(L)


# '''Running sum on list Write a programm  to print a list after performing running sum on it'''

# list1 = [ 1 ,2 , 3, 4, 5, 6]
# sum = 0
# L = []
# for i in list1:
#     sum += i
#     L.append(sum)
# print(L)


# ''''''
# list1 = [ 2 , 4 , 6, 10 , 1]


# L = []
# for i in list1:
#     sum = 0
#     for j in list1:
#         if i<=j:
#             sum += j
#     L.append(sum)
      
# print(L)        


# list1 = [1, 7, 3, 4, 5, 10]
# list2 = [4, 5, 6, 7, 8, 9]

# L = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             # Check if it's already in L to ensure uniqueness
#             if i not in L:
#                 L.append(i)

# L.sort() # Sort once at the end
# print(L) 
# Output: [4, 5, 7]




'''write a list comprehension that can flatten a nested list '''

# L = [[1,2,4],
#           [4,5,6],
#           [7,8,9]]
# s = []

# s = [j for i in L  for j in i   ]
# print(s)

'''write a list comprehension that can transpose a give matrix '''

# matrix = [[1 , 4, 7],
#           [2 , 5 , 8],
#           [3 , 6 , 9]]
# rows = len(matrix)
# col = len(matrix[0])

# T = []
# for i in range(col):
#   row = []
#   for j in range(rows):
#     row.append(matrix[j][i])
#   T.append(row)
# print(T)


'''write a list comprehension to print the following matrix :'''

# matrix = [[0 , 1, 2],[3,4,5],[6,7,8]]

# rows = len(matrix)
# col  = len(matrix[0])

# T = []
# for i in range(rows):
#   T.append([0]*rows)

# for i in range(col):
#   for j in range(rows):
#     T[j][i] = matrix[i][j]

# print(T , end=" ")


'''wap that can find max number of each row of the matrix :'''

# matrix =[ [1 ,2 , 3] , [4,5,6] ,[7,8,9]]
# T = []
# rows = len(matrix)
# col = len(matrix[0])

# for i in range(rows):
#   max_num = matrix[i][0]
#   for j in range(col):
#     if matrix[i][j] > max_num :
#       max_num = matrix[i][j]
#   print("max_num of row" , i , "is : " , max_num)
 
    
''' Write a program that can perform union operation on 2 lists'''

# list1 = [1,2,3,4,5,1]
# list2 =[2,3,5,7,8]
# T = []
# for i in list1:
# 	if i not in T:
# 		T.append(i)

# for j in list2:
# 	if j not in T :
# 		T.append(j)
    
# T.sort()	
# print(T)
  



'''Add Space between Potential Words'''

# str = input("Enter the string:")
# result = str[0]
# for i in  range(1 , len(str)):
#   if str[i].isupper(): 
#     result += " " 
#   result += str[i]
# print(result)
  
'''Convert Character Matrix to single String using string comprehension'''

str = ['CampusX is a channel', 'for data-science', 'aspirants.']
T = []

for i in str:
  word = " "
  for j in i:
    if j != " ":
      word += j
    else :
        T.append(word)
        word = ""
        
  T.append(word) # Append the last word after the loop ends
print(T)















