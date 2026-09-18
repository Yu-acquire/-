class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("describe!")

    def open_restaurant(self):
        print("open!")

my_restaurant=Restaurant('happy','eat')

print("name is "+my_restaurant.restaurant_name.title()+"!")
print("type is "+my_restaurant.cuisine_type.title()+"!")
my_restaurant.open_restaurant()