def leiaDinheiro(stdin):
    while True:
        user = input(stdin)
        if user.isnumeric():
            
            return float(user)
        else:
            print(f'\033[0;31mERRO: \"{user}\" é um preço inválido!\033[m')