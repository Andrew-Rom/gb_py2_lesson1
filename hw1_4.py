"""
HW 1-4
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки.
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
CHECK_LIMIT = 3

num = randint(LOWER_LIMIT, UPPER_LIMIT)
check = 0
print(num)
while check < CHECK_LIMIT:
    choice = input(f'Введите число {LOWER_LIMIT}-{UPPER_LIMIT}: ')
    if choice.isdigit() and LOWER_LIMIT <= int(choice) <UPPER_LIMIT:
        choice = int(choice)
        if choice < num:
            print('Нет. Попробуйте указать большее число \n')
        elif choice > num:
            print('Нет. Попробуйте указать меньшее число \n')
        else:
            print('\nУгадали')
            break
        check += 1
        if check >= CHECK_LIMIT:
            print('\nНе угадали. Попытки кончились')
    else:
        print('\nОшибка ввода. Попытка не учитывается')