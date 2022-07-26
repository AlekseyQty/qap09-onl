# Заменить символ "#" на символ "/" в строке 'www.my_site.com#about'
site = "www.my_site.com#about"
character_replacement = "/"
print(site[:15] + character_replacement + site[15+1:])
