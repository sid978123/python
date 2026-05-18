# '''Here we are going to learn about arrays in python.'''

# '''Maximum sum subarray...'''
L = [ -2 , 4 , 7 , -1 , 6 , -11 , 14 , 3 , -1 , -6]


# d = {}
# for i in range(0 , len(L)):
#   subarray = []
#   for j in range(i ,len(L)):
#     subarray.append(L[j])
#     d[sum(subarray)] = subarray


# max_val = max(d.keys())

# for i in d :
#   if i == max_val :
#     print(d[i])


  

# '''Kaden's Algorithm :'''

# L = [ -2 , 4 , 7 , -1 , 6 , -11 , 14 , 3 , -1 , -6]
# import sys
# curr_sum = 0
# curr_seq = []
# best_sum = -sys.maxsize-1
# best_seq = []
# for i in L :
#   if i+curr_sum > i :
#     curr_sum += i
#     curr_seq.append(i)
#   else :
#     curr_sum = i
#     curr_seq.clear() 
#     curr_seq.append(i)
#   if curr_sum > best_sum :
#     best_sum = curr_sum
#     best_seq = curr_seq
# print(best_seq , best_sum)
  
# '''find element with left side smaller and right side greater in an array :'''

# L = [ 3 , 1 , 2 ,5 , 8 , 7 , 9]


# for i in range(1 , len(L)-1):
#   flag = True

#   for j in range(0 , i):
#     if L[j] > L[i]:
#       flag = False

#   for k in range(i+1 , len(L)):
#     if L[k] < L[i]:
#       flag = False

#   if flag :
#     print(L[i])

    
# ''''''

# for i in range(1 , len(L)-1): #here time complexity is not O(n) , it is   O(n^2)
#   if max(L[:i]) < L[i] < min(L[i+1:]) :
#     print(L[i])



L = [ 3 , 1 , 2 ,5 , 8 , 7 , 9]
# max_arr = []
# max_val = L[0]
# min_val = L[-1]
# min_arr = []  
 
  
# for i in L :
#  if i > max_val :
#    max_val = i
#    max_arr.append(max_val)

# print(max_arr)

# for i in range(len(L) -1 , -1 , -1) :
#   if L[i] < min_val:
#     min_val = L[i]
#   min_arr.insert(0 , min_val)
  
# for i in range(1 , len(L)-1) :
#   if max_arr[i-1] < L[i] < min_arr[i+1]:
#     print(L[i])




'''find continuous sub array with a given sum ( given not negative number : )
return the starting and ending index of the subarray :
return first subarray in case of multiple  :'''

# L = [ 1,22,13,7,9,11,10]
# curr_sum = 0
# for i in L :
#   for j in L[1 ::]:
#     if i + j == 16 :
#       curr_sum = i + j
#       print("index:",(L.index(i),L.index(j)),"=" ,curr_sum)

    
'''maxumum sum sub array :   '''

# L = [ -2 , 4 , 7 , -1 , 6 , -11 , 14 , 3 , -1 , -6]
# d = {}
# for i in range(0 , len(L)):
#   sub_array = []
#   for j in range(i ,len(L) ):
#     sub_array.append(L[j])
#     print(sub_array ,"Sum of Subarray is : " ,sum(sub_array))
#     d[sum(sub_array)] = sub_array


# max_val = max(d.keys())
# for i in d : 
#   if i == max_val :
#     print(d[i])

     
'''Another solution : Kasanes Algorithm'''
# import sys    
# L = [ -2 , 4 , 7 , -1 , 6 , -11 , 14 , 3 , -1 , -6]
# curr_sum = 0
# curr_seq = []
# best_sum = -sys.maxsize-1
# best_seq = []


# for i in L :
#   if i + curr_sum > i :
#     curr_sum = curr_sum + i
#     curr_seq.append(i)


#   else :
#     curr_sum = i 
#     curr_seq.clear()
#     curr_seq.append(i)
    


#   if curr_sum > best_sum :
#     best_sum = curr_sum
#     best_seq = curr_seq
    
 
# print(best_sum , best_seq)

 

'''find element with left side samller and right side greater in an array :'''
  
# L = [ 3, 1, 3, 5, 8, 7, 9]

# for i in range(1 , len(L)-1) :
#   flag = True
#   for j in range(0 , i):
#     if L[j] > L[i]:
#       flag = False

#   for k in range(i+1 , len(L)):
#     if L[k] < L[i]:
#       flag = False

#   if flag:
#     print(L[i])

# '''Another Efficient Approach :'''

# L = [ 3, 1, 3, 5, 8, 7, 9]
# for i in range(1,len(L)-1):
#   if max(L[:i]) < L[i] < min(L[i+1: ]):
#     print(L[i])


  
# L = [ 3, 1, 2, 5, 8, 7, 9]
# max_arr = []
# min_arr = []
# max_val = L[0]
# min_val = L[-1]
# flag = True

# for i in L :
#   if i>max_val :
#     max_val = i 
#   max_arr.append(max_val)

# for i in range(len(L)-1 , -1 , -1 ):
#   if L[i] < min_val :
#     min_val = L[i]
#   min_arr.insert(0 , min_val)


# for i in range(1 ,len(L)-1):
#   if max_arr[i-1] < L[i] < min_arr[i+1]:
#     print(L[i])
  
# print(max_arr)
# print(min_arr) 


'''Find continuous subarray with given sum ( given non negative number )'''
'''retrunn the starting and ending index of the subarray '''
'''return 1st subarray in case of multiple :'''





# L = [1, 22, 13, 7, 9, 11, 10]

# d = {}

# for i in range(len(L)):

#     curr_sum = 0
#     sub_arr = []

#     for j in range(i, len(L)):

#         curr_sum += L[j]
#         sub_arr.append(L[j])

#         if curr_sum == 20:
         
#          d[curr_sum] = sub_arr[:]
            

# print(d)



'''Intersection of the shorted arrays  :'''

# a = [1,2,3,4,5,8]
# b=[3,6,7,8]
# i=j=0
# while i<len(a) and j<len(b):
#    if a[i] == b[j]:
#       print(a[i])
#       i+=1
#       j+=1
      
#    elif a[i]>b[j]:
#       j+=1 

#    else :
#       i+=1


'''Rotate arrays left d items :'''

# L = [ 1,2,3,4,5]
# rotate = 2
# for i in range(rotate):
#     temp = L[0]
#     for j in range(0 , len(L)-1):
     
#       L[j] = L[j+1]
#     L[len(L)-1] = temp 

# print(L)


   
'''Find duplicate items in an array :'''
d = {}
L = [ 1,1,2,3,4,4,5,5]
for i in range(0,len(L)):
  if L[i] not in d.values() :
    d[i] = L[i]

  else :
   
    pass
   
print(d) 

    
'''find first element to occur k times in an array :'''
  
L = [ 1,1,2,3,4,4,5,5]
for  i in L:
  s = L.count(1)
print(s)

   












