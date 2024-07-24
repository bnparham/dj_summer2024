# def sum(*args):
#     res = 0
#     for num in args :
#         res += num
#     return res

# print(sum(2))
# print(sum(2,3))
# print(sum(2,3,4,10,10,0,0,4,5))


# def main(*args, **kwargs):
#     return(kwargs)

# print(main(name='parham', family='bn', age='23'))


# def shopCart(email, *args, **kwargs):
#     print(f'--- USER INFO => {email}---')
#     for k,v in kwargs.items():
#         print(f'{k} : {v}')
#     print(f'Items : {args}')

# shopCart('parham@gmail.com','item1', 'item2', 'item3', 0, True, name='parham', family='bn', age=23)


# print(
#     (lambda *args : sum([num for num in args]))(10,10,7)
# )

# a = [1,2,3,4,5]
# for i in a:
#     b.append(i**2)

# print(set(map(
#     lambda x : x + 10
#     ,
#     a
# )))



# a = [1,2,3,4,5]
# print(list(filter(
#     lambda x : x >= 3
#     ,
#     a
# )))

# a = [1,2,3,4,5]

# print(
#     list(
#             map(
#         lambda x : x ** 2
#         ,
#         filter(
#             lambda x : x >= 3,
#             a
#         )
#     )
#     )
# )

# print([i ** 2 for i in a if i >= 3])