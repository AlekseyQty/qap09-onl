# 2 Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”


list_name_surname = ["Ivan", "Ivanou"]
str_city = "Minsk"
str_country = "Belarus"
list_name_surname = (" ".join(list_name_surname))
print(f'"Привет, {list_name_surname}! Добро пожаловать в {str_city} {str_country}"')