class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or value == '':
            raise value('Name cannot be empty')
        self._name = value
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value > 0 :
            self._salary = value
        else:
            raise ValueError("Salary nust be positive")

e = Employee('ali', 3000)
e.name = 'parham'
e.salary = 5000
print(e.name)
print(e.salary)