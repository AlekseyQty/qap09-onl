# Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

name_surname = ['Ivan', 'Ivanou']
city = "Minsk"
country = "Belarus"

print("Привет, " + " ".join(name_surname) + "! Добро пожаловать в " + city + ", " + country)
