class animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(animal):
    def bark(self):
        print(f"{self.name} is barking.")

my_dog = Dog("Buddy") 

my_puppy = Dog("Max")

my_dog.eat()
my_puppy.bark()

print(my_dog.name)
print(my_puppy.name)

