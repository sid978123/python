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
class Rectangle :
    def __init__(self , l , b):
        self.length = l
        self.breadth = b
        self.area()
        self.is_square()


    def area(self):
        a = self.length*self.breadth
        print("the area of the Rectangle is:" , a )

    def is_square(self):
        if self.length == self.breadth :
            print("the given Rectangle is a square :")

        else : 
            print("the given Rectangle is a Rectangle :")



    @classmethod
    def property(cls, length, breadth):
        return cls(length, breadth)

    
R = Rectangle.property(9 , 9)
        
        

