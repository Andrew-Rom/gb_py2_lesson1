MULTIPLIER_START_NUM = 2
MULTIPLIER_END_NUM = 11
TABLE_START_NUM = 2
TABLE_END_NUM = 10
NUMBER_OF_COLUMNS = 4

# print('ТАБЛИЦА УМНОЖЕНИЯ')
#
for multiplier in range (MULTIPLIER_START_NUM, MULTIPLIER_END_NUM):
    for counter in range(NUMBER_OF_COLUMNS):
        for number in range (TABLE_START_NUM, TABLE_END_NUM):
            print(f'{number} x {multiplier:<2} = {number * multiplier:>2}', end='\t\t')


print()
#
# for multiplier in range (MULTIPLIER_START_NUM, MULTIPLIER_END_NUM):
#     counter = 0
#     for number in range ((TABLE_START_NUM + NUMBER_OF_COLUMNS), TABLE_END_NUM):
#         if counter < NUMBER_OF_COLUMNS:
#             print(f'{number} x {multiplier:<2} = {number * multiplier:>2}', end='\t\t')
#             counter += 1
#         else:
#             print()
#             break
#     print()



