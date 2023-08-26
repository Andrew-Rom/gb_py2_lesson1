# HW 1-1
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

multiplier_start_num = 2
multiplier_end_num = 10
table_start_num = 2
table_end_num = 9
number_of_columns = 4

print('ТАБЛИЦА УМНОЖЕНИЯ'.center(60))

for multiplier in range(multiplier_start_num, multiplier_end_num + 1):
    counter = 0
    for number in range((table_start_num), table_end_num + 1):
        if counter < number_of_columns:
            print(f'{number} x {multiplier:<2} = {number * multiplier:>2}', end='\t\t')
            counter += 1
        else:
            print()
            break

print()

for multiplier in range(multiplier_start_num, multiplier_end_num + 1):
    counter = 0
    for number in range((table_start_num + number_of_columns), table_end_num + 1):
        if counter < number_of_columns:
            print(f'{number} x {multiplier:<2} = {number * multiplier:>2}', end='\t\t')
            counter += 1
        else:
            print()
            break
    print()
