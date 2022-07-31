'''
Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
'''
name = ["Ivan", "Ivanou"]
city = "Minsk"
county = "Belarus"
# print(type(name), type(city)) - Проверка строк и списков
name_str = " ".join(name)
# print(type(name_str)) - Проверка на преоброзование массива в строку
print(f"Привет, {name_str}! Добро пожаловать в {city} {county}")
