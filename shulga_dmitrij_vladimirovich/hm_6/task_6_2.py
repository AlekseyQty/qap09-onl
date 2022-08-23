# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"

def function_change():
    changed_word = []
    for i in range(len(my_word)):
        if my_word[i] not in changed_word:
            changed_word.append(my_word[i])
            if my_word.count(my_word[i]) > 1:
                changed_word.append(str(my_word.count(my_word[i])))

    word_special = "".join(changed_word)
    print(f"{my_word} - {word_special}")

my_word = ""
while my_word != "quit":
    my_word = input("Please enter your word: ")
    my_word = my_word.lower()
    my_word = my_word.replace(" ", "")
    if my_word == "quit":
        print("Goodbye")
    else:

        function_change()
