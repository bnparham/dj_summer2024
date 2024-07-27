# def my_decorator(func):
#     def wrapper():
#         print('bye')
#         func()
#     return wrapper


# @my_decorator
# def say_hello():
#     print('hello')

# say_hello()

# ==============================================================

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'bye')
#         func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def say_hello(name, family, age):
#     print(f'hello {name} {family} | your age is {age}')


# ==============================================================

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"bye {kwargs['name']} {kwargs['family']} | your age is {kwargs['age']}")
#         func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def say_hello(*args, **kwargs):
#     print(f"hello {kwargs['name']} {kwargs['family']} | your age is {kwargs['age']}")

# say_hello(name='ali', family='rezaei', age=30)