'''
💡 Encapsulation is an object-oriented programming principle that restricts direct access to some of an object's components, which can help protect the integrity of the data and ensure that the object's internal state remains consistent. By exposing only necessary methods and properties, encapsulation allows for clean and controlled interactions with user interface (UI) components.

Encapsulation hides the internal state of an object, exposing only what is necessary. This protects the object from unintended interference and misuse.

🚀 Use Cases:

➡️ Banking Systems: In a banking application, encapsulation can hide internal details of account management and expose only necessary methods like deposit and withdraw.

➡️ User Interfaces: Encapsulation allows for clean and controlled interactions with user interface components, ensuring that they function correctly and securely.

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('parham', 10)

p.age = -100

print(p.age)