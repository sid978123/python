
# '''Aggregation'''
# ''' main class ke object me another class ka object pass karna'''

# class Customer :
#   def __init__(self,name,gender,address):
#     self.name = name
#     self.gender = gender
#     self.address = address

#   def print_address(self):
#      print(self.address.get_city(), self.address.pin,self.address.state)

#   def edit_profile(self,new_name,new_city,new_pin,new_state):
#      self.name = new_name
#      self.address.edit_address(new_city,new_pin,new_state)

# class Address :
#     def __init__(self , city , pin,state):
#       self.__city = city 
#       self.pin = pin
#       self.state = state

#     def get_city(self):
#        return self.__city
    
#     def edit_address(self,new_city,new_pin,new_state):
#        self.__city = new_city
#        self.pin = new_pin
#        self.state = new_state
    
 
# add1= Address('gurugram',122011,'haryana')
# cust = Customer("nitish",'male',add1)
# cust.print_address()
# cust.edit_profile('siddharth','auraiya',206244,'up')
# cust.print_address()

'''Inheritance :'''

class User:
   def __init__(self):
      self.name = 'siddharth'
   def login(self):
      print("user logged in successfully ;")

  
class Student(User):
  #  def __init__(self):
  #     super().__init__(self.name)
  #     self.roll = 1234

   def print_roll(self):
      print("roll no is",self.roll)


s = Student()
print(s.name)




'''***************************************'''
'''firstly it will run the child class constructer , if child class has no any constructer then it will run the parent class constructer :'''

# class Phone:
#    def __init__(self , price,brand,camera):
#       self.brand = brand
#       self.price = price 
#       self.camera = camera

#    def show(self):
#       print(self.price)
# class Smartphon(Phone):
#    def check(self):
#       print(self.price)
     
# s = Smartphon(30000, "Apple",13)
# s.show()


# '''*******************************'''
# class Parent :
#    def __init__(self, num):
#       self.__num = num
#    def get_num(self):
#       return self.__num
   

# class child(Parent):
#    def __init__(self,val,num):
#       self.__val = val

#    def get_val(self):
#       return self.__val
   

# son = child(100, 10)
# print("parent: Num",son.get_num())
# print("child: Val:" , son.get_val())

'''***********Method Overriding **************************'''

# class Phone:
#    def __init__(self,price,brand,camera):
#       self.price = price
#       self.brand = brand
#       self.camera = camera

#    def buy(self):
#       print("Buying a phone :")

# class Smartphone(Phone):
#    def buy(self):
#       print("buyinbg a smartphone")

# c = Phone(20000, "apple" , 13)
# s = Smartphone(20000, "apple" , 13)
# s.buy()


'''Super Keyboard :'''

class Phone:
   def __init__(self,price,brand,camera):
      print("inside phone constructer :")
      self.__price = price
      self.__brand = brand
      self.__camera = camera

   

class Smartphone(Phone):
   def __init__(self,price ,brand,camera,os,ram):
      print("inside samrtphone constructer :")
      super().__init__(price , brand , camera)
      self.os = os
      self.ram = ram

   print("inside smartphone constructer :")

s = Smartphone(2000, 'samsung',12,"Android" ,2)
print(s.os)
print(s.ram)
   








