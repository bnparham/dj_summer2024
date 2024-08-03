""""
💡 Understanding the basics of OOP is essential for building more complex software. It provides the groundwork for organizing code in a modular and reusable way.

🚀 Use Cases:
➡️ Software Development: Most modern software, including web applications, desktop apps, and games, uses OOP principles.

➡️ Maintenance and Extensibility: OOP promotes code that is easier to maintain and extend, which is crucial for large-scale applications.

"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f'{self.name} says woof!'
    
my_dog = Dog('Alex', 5)

print(my_dog.name)

print(my_dog.bark())