MULTIPLIER_START_NUM = 2
MULTIPLIER_END_NUM = 11
TABLE_START_NUM = 2
TABLE_END_NUM = 10
NUMBER_OF_COLUMNS = 4
for multiplier in range (MULTIPLIER_START_NUM, MULTIPLIER_END_NUM):
    for number in range (TABLE_START_NUM, TABLE_END_NUM):
        print(f'{number} x {multiplier:<2} = {number * multiplier:>2}', end='\t\t')
    print()


