# برای تابع  profile_page یک دیکوریتور احراز هویت اضافه کنید
# بررسی شود کاربر لاگین کرده است یا خیر 
# نام دیکوریتور برابر با is_login میباشد
# برای شبیه سازی این امر، کاربرانی که None هستند لاگین نکرده اند


# USER = None
# USER = 'parham@gmail.com'

# def is_login(func):
#     def wrapper():
#         if USER:
#             func()
#         else:
#             print('Eror 404')
#     return wrapper

# @is_login
# def profile_page():
#     print('this is profile page')

# profile_page()