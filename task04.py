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


list1 = [1, 7, 3, 4, 5, 10]
list2 = [4, 5, 6, 7, 8, 9]

L = []
for i in list1:
    for j in list2:
        if i == j:
            # Check if it's already in L to ensure uniqueness
            if i not in L:
                L.append(i)

L.sort() # Sort once at the end
print(L) 
# Output: [4, 5, 7]




