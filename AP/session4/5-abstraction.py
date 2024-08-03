"""
💡 Abstraction provides a simplified interface by hiding complex implementation details, allowing users to interact with objects at a higher level.

The main goal of abstraction is to reduce complexity and allow for efficient design and implementation of complex systems by focusing on the essential features and behavior of an object rather than its implementation.

🚀 Use Cases:

➡️ Database Systems: Abstraction allows for interaction with different types of databases (e.g., SQL, NoSQL) through a common interface, without needing to understand the specifics of each database.

➡️ API Design: Abstraction is used in designing APIs, where users interact with high-level functions and methods without knowing the internal workings.


"""
from abc import abstractmethod, ABC

class Car(ABC):

    @abstractmethod
    def start(self):
        return '1'

    @abstractmethod
    def stop(self):
        return '2'

class Tesla(Car):
    def start(self):
        return 'tesla start'
    def stop(self):
        return 'tesla stop'

c = Car()
print(c.start())

# tesla = Tesla()
# print(tesla.start())