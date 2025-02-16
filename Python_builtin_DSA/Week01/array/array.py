# here  is concepts of memory when we creat calss


class Product:
    brand =  'Apple'   # it called class attribute

    def __init__(self, name):    # magic method / dunder method/ constructor / initializer
        self.name = name      # it called instance attribute

    def display(self):
        print(f"Product name: {self.name}, Brand: {self.brand}")


p1 = Product("laptop")  # p1 is object or object name of Product class or instance of Product class
print(p1.display())
p2 = Product("Mobile")
print(p2.display())

# every object has its own memory location  now explain with example

# first create a global memory in our memory for class Product
# then further create two type of memory stack and heap memory
# stack memory is used for storing the reference of the object and heap memory is used for storing the object

# stack memory
# p1 = Product("laptop")  # p1 is object or object name of Product class or instance of Product class
# p2 = Product("Mobile")
# stack memory is used for storing the reference of the object
# p1 and p2 are reference of object


# heap memory
# Product class is created in heap memory
# Product class has two attribute brand and __init__ method and display method
# Product class has two object p1 and p2 in heap memory with their own memory location
# p1 and p2 has its own memory location in heap memory with their own attribute name



# brand is class attribute and it sharable to all object of class Product and it is stored in class memory
# like we can access class attribute with class name or object name of class(Product, p1, p2)
# p1.brand = 'Apple'  # it is instance attribute and it is stored in object memory
# p2.brand = 'Apple'  # it is instance attribute and it is stored in object memory
# Product.brand = 'Apple'  # it is class attribute and it is stored in class memory

# name is instance attribute and it is stored in object memory and it is not sharable to all object of class Product
# like we can access instance attribute with object name of class(Product, p1, p2)
# p1.name = 'laptop'  # it is instance attribute and it is stored in object memory
# p2.name = 'Mobile'  # it is instance attribute and it is stored in object memory
# Product.name = 'laptop'  # it is instance attribute and it is stored in object memory

# display is instance method and it is stored in class memory and it is sharable to all object of class Product
# like we can access instance method with object name of class(Product, p1, p2)


def array(param, param1):
    return None