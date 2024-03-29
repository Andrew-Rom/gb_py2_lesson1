"""
HW 1-3
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

num = input('Введите натуральное число, меньше 100 тыс.: ')
if num.isdigit() and 0 < int(num) <= 100_000:
    num = int(num)
    check = True
    if num > 2 and not num % 2:
        check = False
    else:
        for i in range(3, num, 2):
            if num % i == 0:
                check = False
                break
    print(f'{num} - целое') if check else print(f'{num} - составное')
else:
    print('Ошибка ввода')
