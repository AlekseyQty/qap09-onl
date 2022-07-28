# *2) Дан текст, который содержит различные английские буквы и знаки препинания.
# Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a".
# Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите.
# Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".

string = "Hhhhhello World! One Ops AAaa + 900 * 5"
string_d = string.lower()
string_dif = string_d.replace(" ", "")
print(string_dif)
unique = {}
for i in string_dif:
    if i in unique:
        unique[i] += 1
    else:
        unique[i] = 1
max_value = max(unique.values())
for key in unique:
  if unique[key] == max_value:
      print(f"Most repeated character: {key}-{unique[key]}")




