with open('1.txt', 'r', encoding = 'utf - 8') as file:
    data = file.read()
    print(data)
    authoe = input('Введіть автора:')
    with open('1.txt', 'r', encoding = 'utf - 8') as file:
        file.write(author)
