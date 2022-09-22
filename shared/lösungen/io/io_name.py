while True:
    name = input('Bitte geben Sie Ihren Namen ein: ')
    if name.strip().lower() == 'end':
        print('Tschüß')
        break
    print(f'Hallo: {name}')