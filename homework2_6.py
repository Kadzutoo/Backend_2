#Функция пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Обмен элементов
    return arr


#Функция двоичного поиска
def binary_search(val, arr):
    first = 0
    last = len(arr) - 1
    result_ok = False
    pos = -1  # Для хранения позиции найденного элемента

    while first <= last:
        middle = (first + last) // 2
        if val == arr[middle]:
            result_ok = True
            pos = middle
            break
        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f"Элемент найден на позиции: {pos}")
    else:
        print("Элемент не найден")


# Пример работы функций:
unsorted_list = [39, 7, 23, 32, 5, 67]
print("Неотсортированный список:", unsorted_list)

# Применяем функцию сортировки
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

# Применяем функцию двоичного поиска
binary_search(23, sorted_list)  # Ищем элемент 23
