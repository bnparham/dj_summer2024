# سناریو 2: دیتا های یک فروشگاه در دسترس ما قرار گرفته و قراره آنالیز های زیر روی دیتا انجام بدیم

# بررسی تمام کاربران سبد خرید کامل دارند یا خیر

# لیستی از نام و نام خانوادگی کسانی که سبد خرید آنها تکمیل است

# ساخت دیشکنری که کلید شامل نام کاربر و ولیو شامل قیمت نهایی باشد


price = {
    'django': 10,
    'js': 4,
    'python': 6,
}

persons = [
    {'name': 'parham', 'family': 'bn', 'age': 23, 'shopCart': ['django']},
    {'name': 'kia', 'family': 'gr', 'age': 21, 'shopCart': []},
    {'name': 'sara', 'family': 'mn', 'age': 28, 'shopCart': []},
    {'name': 'alex', 'family': 'hs', 'age': 32, 'shopCart': ['python', 'js']},
    {'name': 'maria', 'family': 'lo', 'age': 25, 'shopCart': ['django', 'python']},
    {'name': 'john', 'family': 'doe', 'age': 45, 'shopCart': []},
    {'name': 'emma', 'family': 'ng', 'age': 30, 'shopCart': ['js', 'django', 'python']},
    {'name': 'liam', 'family': 'sm', 'age': 27, 'shopCart': []},
    {'name': 'noah', 'family': 'jd', 'age': 22, 'shopCart': ['js']},
    {'name': 'ava', 'family': 'pt', 'age': 24, 'shopCart': []},
    {'name': 'oliver', 'family': 'lk', 'age': 26, 'shopCart': []},
    {'name': 'amelia', 'family': 'bw', 'age': 29, 'shopCart': ['python']}
]
