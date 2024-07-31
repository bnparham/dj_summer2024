class Car():

    number_of_door = 4


    def start(self):
        print('car started - 2!')

class Benz(Car):
    def say_hello(self, name):
        return f'hello {name}'
    
a = Car()
a.start()

benz = Benz()
benz.start()
print(benz.say_hello('benz'))