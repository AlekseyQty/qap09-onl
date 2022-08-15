# Напишите декоратор, который считает сколько времени работала декорируемая функция. Для получения текущего времени
# можно использовать функцию time.time(). Для того чтобы искусственно замедлить работу функции можно использовать
# time.sleep()

import time

delay = ""
while delay != "quit":
	delay = input("Please enter your time sleep: ")

	if delay == "quit":
		print("Goodbye")
	else:
		delay = int(delay)
		def timeit(func):

			def wrapper(delay):

				func(0)
				print(f" Time work: {round(time.time(), 2)}")
				func(delay)
				print(f" Time work: {round(time.time(), 2)}")

			return wrapper

		@timeit
		def my_func(delay):

			number = 3
			factorial = 1
			for i in range(1, number + 1):
				if i > 1:
					factorial *= i
				else:
					factorial = 1
			print(f" Factorila: {factorial}")
			time.sleep(delay)


		my_func(delay)




