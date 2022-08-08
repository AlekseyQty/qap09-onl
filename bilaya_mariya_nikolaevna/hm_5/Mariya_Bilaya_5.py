# Like. Cоздайте программу, которая, принимая массив имён, возвращает строку описывающая
# количество лайков (как в Facebook).

print(("-" * 25) + "Likes" + ("-" * 25))

likes = ["Alex", "Mark"]
x = len(likes)
print("len of likes:", x)
if x == 0:
    print("no one likes this")
elif x == 1:
    print(f"{likes[x-1]} likes this")
elif x == 2:
    print(" and ".join(likes) + " " + "like this")
elif x == 3:
    print(f"{likes[x-3]}, {likes[x-2]} and {likes[x-1]} like this")
elif x > 3:
    print(f"{likes[0]}, {likes[1]} and 2 others like this")


# Напишите программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3
# она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5  печатать "Buzz".
# Для чисел которые кратны 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.

print(("-" * 25) + "BuzzFuzz" + ("-" * 25))


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("BuzzFuzz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)









