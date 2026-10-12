def greet():
    print("Hello, welcome to the Python project!")
    print("This project demonstrates the use of sets, dictionaries, lists, and tuples in Python.")

greet()
greet()

def check_weather(n):  
    if n > 30:
        print("It's a hot day!")
    else:
        print("It's a cool day!")

check_weather(25)
check_weather(35)
check_weather(12)

def calculate_price():
    price = 10
    tax = 0.2
    print(f"The total price is: {price + tax}")

calculate_price()

def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")

# Call with values
introduce("Omkar", 21)
introduce("Aditya", 16)

