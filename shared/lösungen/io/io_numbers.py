with open('numbers.txt', 'w') as fobj:
    for number in range(1, 11):
        fobj.write(f'{number}\n')