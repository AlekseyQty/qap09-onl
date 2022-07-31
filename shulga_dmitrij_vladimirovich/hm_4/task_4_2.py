# 2.Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

my_name = ["Ivan", "Ivanou"]
string_first = "Minsk"
string_two = "Belarus"
print(f"Привет {' '.join(my_name)}! Добро пожаловать в {string_first} {string_two}")