# ДЗ урок 3  "Стиль кода часть II. Цикл While." module_2_3.py
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while (index < len(my_list)) and (my_list[index] >= 0):
    if my_list[index] != 0:
        print(my_list[index])
    index += 1
    continue

