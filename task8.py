# class Car :
#   __counter = 0 

#   def __init__(self):
#     Car.__counter += 1 

#   def get_counter ():
#     return Car.__counter
  

# o1 = Car() 
# o2 = Car() 
# o3 = Car() 
# o4 = Car() 

# print(Car.get_counter())



# import random

# class Cards:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value

#     def __repr__(self):
#         return "{}->{}".format(self.suit, self.value)


# class Deck:
#     def __init__(self):
#         suits = ['Heart', 'Diamond', 'Club', 'Spades']
#         values = ['A', '2', '3', '4', '5', '6', '7',
#                   '8', '9', '10', 'J', 'Q', 'K']

#         self.card = [Cards(suit, value)
#                      for suit in suits
#                      for value in values]

#     def __str__(self):
#         return f"Cards left: {len(self.card)}"

#     def shuffle(self):
#         if len(self.card) < 52:
#             print("Only full deck can be shuffled")
#         else:
#             random.shuffle(self.card)

#     def deal(self):
#         if len(self.card) == 0:
#             return "No cards left"
#         return self.card.pop()


# deck = Deck()
# deck.shuffle()

# print(deck.deal())
# print(deck)


'''Find area of the rectangle  :'''
# class Rectangle :
#     def __init__(self , l , b):
#         self.length = l
#         self.breadth = b
#         self.area()
#         self.is_square()


#     def area(self):
#         a = self.length*self.breadth
#         print("the area of the Rectangle is:" , a )

#     def is_square(self):
#         if self.length == self.breadth :
#             print("the given Rectangle is a square :")

#         else : 
#             print("the given Rectangle is a Rectangle :")



#     @classmethod
#     def property(cls, length, breadth):
#         return cls(length, breadth)

    
# R = Rectangle.property(9 , 9)

# '''We have to write a prog that uses a date time module and it also uses : '''

# import datetime
# class Product :
#     def __init__(self):
#         self.manufacture_date = input("Enter manufacturing date (mm/dd/yyyy)")
#         self.expiry_date = input("Enter expiry date (mm/dd/yyyy)")
#         self.manufacture_date = datetime.datetime.strptime(self.manufacture_date , '%m/%d/%Y')
#         self.expiry_date = datetime.datetime.strptime(self.expiry_date , '%m/%d/%Y')

#     def time_to_expire(self):
#         today = datetime.datetime.now()
#         if today > self.expiry_date :
#             print("product expired already : ")

#         else :
#             time_left = self.expiry_date.date() - today.date()
#             print(time_left)


# obj = Product()
# obj.time_to_expire()


'''*********************************************'''

# class Student :
#   def __init__(self):
#     self.__sid = None
#     self.__marks = None
#     self.__age = None

#   #setters methods are creatinh ;
#   def set_sid(self , sid):
#     self.__sid  = sid
#   def set_marks(self , marks):
#     self.__marks= marks
#   def set_age(self , age):
#     self.__age  = age


#   #Now we write getter : 

#   def get_sid(self):
#     return self.__sid
  
#   def get_marks(self):
#     return self.__marks
  
#   def get_age(self):
#     return self.__age
  

#   def validate_age(self):
#     return self.__age>20 ;

#   def validate_marks (self):
#     return  self.__marks >= 0 and self.__marks <= 100 
  
#   def check_qualification(self) :
#     if self.validate_age() and self.validate_marks():
#       return True
    
#     else :
#       return False


# stu1 = Student()
# stu1.set_sid(101)
# stu1.set_age(21)
# stu1.set_marks(66)

# print(stu1.get_age())
# print(stu1.get_marks())
# print(stu1.get_sid()) 
# print(stu1.check_qualification())



# '''**********************************'''
# class Scoop :
#   def __init__(self, flavor , price):
#     self.flavor = flavor
#     self.__price  = price 

    
# class Bowl :
#   def __init__(self):
#     self.__scoop_list =  []

  
#   def add_scoop(self , *new_scoops):
#     for scoop in new_scoops :
#       self.__scoop_list.append(scoop)

#   def display(self):
    
#     for scoop in self.__scoop_list:
#       print()
    

# obj = Scoop("chocklate")

'''***********************'''
#Aggregation

'''It means has a  relationship :'''
 
class Customer:
  def __init__(self, name,gender,address):
    self.name = name
    self.address = address
    self.gender = gender
  def print_address(self):
    print(self.address.city , self.address.pin,self.Address.state)

class Address:
  def __init__(self,city , pincode,state):
    self.city = city
    self.state = state
    self.pincode = pincode
add1 = Address('gurugram','122011','haryana')
cust = Customer('nitish','male' ,add1)
cust.print_address()










