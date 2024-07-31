class Car():

    # Year = 2024
    # Color = 'black'
    # Power = '288 hp'

    def __init__(self, Year, Color, Power):
        self.Year = Year
        self.Color = Color
        self.Power = Power
        self.balance = 10000

    def start(self):
        print('car moved !')

    def stop(self):
        print('car stopped !')

    def say_hello(self, name):
        return f'hello {name}'


a = Car(2024, 'black', '288 hp')
print(a.Year)
print(a.Color)
print(a.Power)
a.start()
a.stop()
print(a.say_hello('bmw'))

print('======================================================')
print('======================================================')

b = Car(1999, 'red', '100 hp')
# b.Color = 'white'
# b.Year = 1999
# b.Power = '100 hp'
# b.is_new = False

print(b.Year)
print(b.Color)
print(b.Power)
# print(b.is_new)
# b.start()
# b.stop()