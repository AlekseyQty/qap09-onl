def reshape(array, height, width):
    """Функция для создания матриц из одномерного массива"""
    iter_value = iter(array)
    new_arr = []
    if height * width == len(array):
        for i in range(height):
            new_arr.append([next(iter_value) for elem in range(width)])

        for elem in new_arr:
            print(elem)
    else:
        print("Ошибка, такая матрица не может быть построена")


reshape([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
