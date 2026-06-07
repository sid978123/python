# # my_set = { 1, 2, 3, 4,'hello' , 'hey'}
# # my_set = { 1, 2, 3, 4,4,4,4,4,'hello' , 'hey'}
# # print(my_set)

# # sett =[2,2, 3, 4,5 ,6]
# # set1 = set(sett)
# # print(set1)

# # print(set1)
# # set1.pop()
# # set1.pop()
# # set1.pop()
# # set1.clear()

# # print(set1)


# # a = { 2 , 3, 4, 98, 6}
# # b = {3 ,3 ,4 , 5, 6}

# # d = a.union(b)
# # print(d)
# # print(a|b)


# # a = { 2 , 3, 4, 98, 6}
# # b = {3 ,3 ,4 , 5, 6}

# # print(a-b)
# # print(b.difference(a))
# # print(a.difference(b))

# a = { 2 , 3, 4, 98, 6}
# b = {3 ,56 ,4 , 5, 6}

# d = b.copy()
# print(d)
# d.add(67)
# print(d)

# e = b.intersection(a)
# print(e)


# # p = a.symmetric_difference(b) # it return the value which afer return in both set even after removing the same element in the both set :
# # print(p)


# # a = { 2 , 3, 4, 98, 6}
# # a = {2,3,4 ,2, 4,96}
# # b  = { 2 , 3, 4}
# # print(b.issuperset(a)
# # )

# # d = {'name':"jack" , 'age':26}
# # print(d['name'])
# # d['roll'] = 43
# # print(d)
# # d['enroll'] = 23036363
# # print(d)
# # print(d)

# # d.pop('age')
# # print(d)
# marks = {}.fromkeys(['math' , 'english' , 'science' ] ,  23)
# print(marks)


# squares = {1:1 , 2:4 ,4:16}
# print(2 in squares)
# print(3 in squares)
# print(98 in squares)


# a = { 2 , 3, 4, 98, 6}
# b = {3 ,56 ,4 , 5, 6}

# d = b.copy()
# print(d)
# d.add(67)
# print(d)

# e = b.intersection(a)
# print(e)


# p = a.symmetric_difference(b) # it return the value which afer return in both set even after removing the same element in the both set :
# print(p)





# class Atm:

#     def __init__(self):
#         self.pin = ""
#         self.balance = 0
#         self.menu()
        

#     def menu(self):
#         user_input = input('''
# Hi, how can I help you:
# 1. Press 1 to create pin
# 2. Press 2 to change pin
# 3. Press 3 to check balance
# 4. Press 4 to withdraw
# 5. Anything else to exit
# ''')

#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.change_pin()
#         elif user_input == "3":
#             self.check_balance()
#         elif user_input == "4":
#             self.withdraw()
#         else:
#             exit()

#     def create_pin(self):
#         user_pin = int(input("Enter pin: "))
#         self.pin = user_pin

#         user_balance = int(input("Enter balance: "))
#         self.balance = user_balance

#         print("Pin created successfully")
#         self.menu()

#     def change_pin(self):
#       old_pin = int(input("Enter old pin :"))
#       if old_pin == self.pin :
#         new_pin = int(input("Enter new pin :"))
#         self.pin = new_pin
#         print("Pin changed successfully :")
#         self.menu() 
#       else :
#         print("Nahi karne de sakta re Baba :")
#         self.menu()


#     def check_balance(self):
#       user_pin = int(input("Enter Pin :"))
#       if user_pin == self.pin :
#          print("balanced fetched successfully : " , self.balance)

#       self.menu()

#     def withdraw(self):
#       user_pin = int(input("Enter the pin : "))
#       if user_pin == self.pin :
#         with_money = int(input("Enter the amount you want to withdraw :"))
#         if with_money <= self.balance :
#             self.balance -= with_money
#             print("Balance withdrawn successfully :")
#             print("Remaining Balance is :", self.balance)
#         else:
#             print("Insufficient balance.")
#         self.menu()
           

#       else :
#          print("Enter the correct Pin to withdraw the money :")
      

# obj = Atm()
# obj.menu()






# **************Methods VS function********************

'''The true use of constructer is to write configuration related code   '''

'''Constructor is a special method which is automatically called when an object of a class is created . It is used to initialize the attributes of the class .'''

'''**************Self*************'''
'''Self is nothing but the current object :'''

# class Fraction :
#    def __init__(self , x , y):
#       self.num = x 
#       self.den = y

#    def __str__(self):
#        return '{}/{}'.format(self.num , self.den)
   
#    def __add__(self , other):
#       new_num =self.num*other.den + other.num*self.den
  
# fr1 = Fraction(1 , 2)
# fr2 = Fraction(1 , 2)
# print()


class Point :
  def __init__(self , x , y ) :
    self.x_cod = x 
    self.y_cod = y 

p1 = Point(1 , 3)
print(p1)






   













