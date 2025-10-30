class product:
    #private class variable
    

    def __init__(self,input_name, input_price):
        self.name = input_name
        self.price = 0
        self.quantity = 0

#Get method
def get_price(self):
    return self.price


    #Set method
def set_price(self, value):
    if value >= 0:
        self.price = value

  #Set method
def set_quantity(self, value):
    if 0 <= value <99:
        self.quantity = value
    
    
    #build in print method

    def __str__(self):
        return f"product Name: {self.name}, Price: {self.price}"
#create a product with name
apple_iphone = product("iPhone 19 pro max")
apple_watch = product("Apple Watch Series 10")

#set the price
apple_iphone.set_price(999.99)
apple_watch.set_price(499.99)

#set the quantity
apple_iphone.set_quantity(10)
apple_watch.set_quantity(3)

#print the product details
print(apple_iphone)
print(apple_watch)

