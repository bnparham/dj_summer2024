# مشابه پیاده سازی سناریو سوم ، فیچر در دسترس بودن صفحه نیز اضافه شود


# USER = None
USER = 'parham@gmail.com'

def is_login(show_page):
    def inner_decorator(func):
        def wrapper():
            if show_page:
                if USER:
                    func()
                else:
                    print('you must login first !')
            else:
                print('page not found !')
        return wrapper
    return inner_decorator

@is_login(False)
def profile_page():
    print('this is profile page')

profile_page()