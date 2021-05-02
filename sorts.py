#------------------------------------------------------------------------------#
#-------------------------------  Модули  -------------------------------------#
#------------------------------------------------------------------------------#



# Модуль для обработки скорости выполнения сортировки
import time
# Модуль для перемешивания, создания рандомных: чисел, строк и т.д
import random
# Модуль для импортирования таблицы ASCII
import string
# Модуль для использования многопоточности
import threading

import asyncio

#------------------------------------------------------------------------------#
#------------------------  Глобальные переменные  -----------------------------#
#------------------------------------------------------------------------------#



<<<<<<< Updated upstream
# [числа] Динамический список от 0 до 50000
array_dynamic_num = [random.random() * 5000 for i in range(5000)]

# [строки] Динамический список от 0 до 3500
array_dynamic_str = list(' '.join(random.choice(string.ascii_lowercase) for i in range(3500)))
=======
# [числа] Динамический список от 0 до 3000
array_dynamic_num = [random.random() * 3000 for i in range(3000)]

# [строки] Динамический список от 0 до 10000
array_dynamic_str = list(' '.join(random.choice(string.ascii_lowercase) for i in range(3000)))
>>>>>>> Stashed changes



#------------------------------------------------------------------------------#
#----------------------------  Основной код  ----------------------------------#
#------------------------------------------------------------------------------#



def decorator_testing_speed(sort):

    '''======================================================'''
    '''     Декоратор для измерения скорости исполнения      '''
    '''======================================================'''

    def speed_measurement(array):

        # Точка отсчёта
        start_time = time.time()

        # Исполнение функций
        name_sort = sort(array)

        # Точка подсчёта итоговой скорости исполнения
        total_speed = time.time() - start_time
        print(f'{name_sort} - завершилась за: {str(total_speed)[:8]} \n')

    return speed_measurement



class Sorts():


    @decorator_testing_speed
    def bubble_sort(array):

        '''=================================='''
        '''     1) Cортировка пузырьком      '''
        '''=================================='''

        swaps = True

        while swaps:

            swaps = False

            for j in range(len(array)-1):
                if array[j] > array[j+1]:
                    swaps = True
                    array[j], array[j+1] = array[j+1], array[j]

        return f'[cортировка пузырьком]'



    @decorator_testing_speed
    def selection_sort(array):

        '''=================================='''
        '''      2) Сортировка выбором       '''
        '''=================================='''

        for i in range(len(array)):
            minimum = i

            for j in range(i + 1, len(array)):

                # Выбор наименьшего значения
                if array[j] < array[minimum]:
                    minimum = j

            # Помещаем это перед отсортированным концом массива
            array[minimum], array[i] = array[i], array[minimum]

        return f'[сортировка выбором]'



    @decorator_testing_speed
    def insertion_sort(array):

        '''=================================='''
        '''     3) Сортировка вставками      '''
        '''=================================='''

        for i in range(len(array)):
            cursor = array[i]
            pos = i

            while pos > 0 and array[pos - 1] > cursor:

                # Меняем местами число, продвигая по списку
                array[pos] = array[pos - 1]
                pos = pos - 1

            # Остановимся и сделаем последний обмен
            array[pos] = cursor

        return f'[сортировка вставками]'



#------------------------------------------------------------------------------#
#-------------------------------  Запуск  -------------------------------------#
#------------------------------------------------------------------------------#

<<<<<<< Updated upstream
START = Sorts.bubble_sort(array_dynamic_num)
print(START)


# Автор: Орлов Евгений
=======
# [Test speed - numbers]
START = asyncio.run(Sorts.bubble_sort(array_dynamic_num))
START_02 = asyncio.run(Sorts.bubble_sort(array_dynamic_num))
>>>>>>> Stashed changes
