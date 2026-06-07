class Point :
  def __init__(self , x , y ) :
    self.x_cod = x 
    self.y_cod = y 
  # def __str__(self):
  #   return '<{},{}>'.format(self.x_cod , self.y_cod)
  
  # def euclidean_distance(self , other):
  #   return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
  
  # def dis_from_origin(self):
  #   return self.euclidean_distance(Point(0,0))

# p1 = Point(1,1)
# p2 = Point(10, 10)
# p3 = p1.euclidean_distance(p2)
# p4 = p1.dis_from_origin()
# print(p4)



class Line:
  def __init__(self,A,B,C):
    self.A = A
    self.B = B
    self.C = C
  
  def __str__(self):
    return '{}x + {}y + {} = 0 '.format(self.A , self.B , self.C)
  
  def point_on_line(line , Point):
    if line.A*Point.x_cod + line.B*Point.y_cod + line.C == 0 :
      return "Lies on the line"
    else :
      return " does not lie on the line"
    

  def shortest_distance(line , Point):
    return (line.A*Point.x_cod + line.B*Point.y_cod + line.C)/((line.A)**2 + (line.B)**2)**0.5
  
l1 = Line(1,1,-2)
p1 = Point(1,1)
A = l1.point_on_line(p1)
B = l1.shortest_distance(p1)
print(B)
# print(A)
# print(l1)
# print(p1)

'''when two line intersect'''
 


'''pass by reference '''
'''Encapsulation :'''

class Atm:
    counter = 1

    def __init__(self):
        self.__pin = ""
        self.balance = 0
        self.cid = Atm.counter
        Atm.counter = Atm.counter + 1
        # self.menu()
    def get_balance(self):
       return self.balance
       
    def set_balance(self , new_value):
       if type(new_value) == int:
          self.balance = new_value
       else :
          print("sale chor : ")    
        

    def menu(self):
        user_input = input('''
Hi, how can I help you:
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Press 5 to get the balance
6> Press 6 to se the balance :                           
7. Anything else to exit
                           
''')

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        elif user_input == "5":
            self.get_balance()
        elif user_input == "6":
            self.set_balance()
        
        else:
            exit()

    def create_pin(self):
        user_pin = int(input("Enter pin: "))
        self.pin = user_pin

        user_balance = int(input("Enter balance: "))
        self.balance = user_balance

        print("Pin created successfully")
        self.menu()

    def change_pin(self):
      old_pin = int(input("Enter old pin :"))
      if old_pin == self.pin :
        new_pin = int(input("Enter new pin :"))
        self.pin = new_pin
        print("Pin changed successfully :")
        self.menu() 
      else :
        print("Nahi karne de sakta re Baba :")
        self.menu()


    def check_balance(self):
      user_pin = int(input("Enter Pin :"))
      if user_pin == self.pin :
         print("balanced fetched successfully : " , self.balance)

      self.menu()

    def withdraw(self):
      user_pin = int(input("Enter the pin : "))
      if user_pin == self.pin :
        with_money = int(input("Enter the amount you want to withdraw :"))
        if with_money <= self.balance :
            self.balance -= with_money
            print("Balance withdrawn successfully :")
            print("Remaining Balance is :", self.balance)
        else:
            print("Insufficient balance.")
        self.menu()
           

      else :
         print("Enter the correct Pin to withdraw the money :")


    
      

c1 = Atm()
c2 = Atm()
c3 = Atm()

print(c1.cid)
print(c2.cid)
      

# obj = Atm()
# obj.menu()
# p1 = obj.set_balance(10000)
# p2 = obj.get_balance()
# p1 = obj.set_balance("ehehheh")
# p3 = obj.get_balance()

# print(p2)
# print(p3) 





'''collection of the Objects :'''


class Person :
  

  def __init__(self, name,gender):
    self.name = name
    self.gender = gender
  


p1 = Person('nitish' , 'male')
p2 = Person('ankit' , 'male')
p3 = Person('ankita' , 'female')

L = [p1,p2,p3]
d = {'p1':p1 , 'p2':p2 , 'p3':p3}
for i in L:
  print(i.name , i.gender)

for i in d :
  print(d[i].gender)



 
''''static variable :'''

class Atm:
  counter = 1



'''static method : '''

@staticmethod
def get_counter ():
   return Atm.counter







