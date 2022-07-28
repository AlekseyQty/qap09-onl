#Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
#Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

list_1 = ["Ivan ", "Ivanou"]
str_1 = "Minsk"
str_2 = "Belarus"

print(f"Привет, {''.join(list_1)}! Доброе пожаловать в {str_1} {str_2}")