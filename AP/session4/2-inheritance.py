"""
💡 Inheritance allows for the creation of new classes based on existing ones, promoting code reuse and reducing redundancy.

🚀 Use Cases:

➡️ Game Development: Inheritance can be used to create various types of characters or objects that share common attributes and behaviors but also have unique features.

➡️ Frameworks and Libraries: Many libraries and frameworks use inheritance to provide base classes with common functionalities that can be extended or customized.

"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Animal Sound'
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

my_cat = Cat('Alex')
print(my_cat.name)
print(my_cat.speak())