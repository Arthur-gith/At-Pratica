from random import randint
from random import seed
from time import sleep
#importanto as funções das bibliotecas.

cadastro = []
seed(100)

print('-' * 20, 'MENU', '-' * 20)
print('1 - Nova inscrição ')
print('2 - Vizualizar inscrição ')
print('0 - Encerrar ')
while True:
    pessoa = {}
    # Garantindo que a opção digitada seja do tipo inteiro
    while True:
        try:
            op = int(input('Escolha uma opção: '))
            while (op != 1) and (op != 2) and (op != 0):
                print('Digite uma das opções válidas.')
                op = int(input('Escolha uma opção: '))
            break
        except ValueError:
            print('ERRO! somente numeros inteiros, conforme o menu anterior...')

    if op == 1:

        # coleta os dados de cadastro e insere na estrutura do dicionario

        pessoa['voucher'] = randint(100, 400)
        pessoa['nome'] = input('Nome: ')

        # validando o email antes de inserir na estrura pessoa
        email = input('Digite seu e-mail:')
        while True:
            if not ('@' in email) or not ('.' in email):
                print('E-mail inválido, digite novamente.')
                email = input('Digite seu e-mail: ')
            else:
                pessoa['email'] = email
                break

        pessoa['telefone'] = input('Telefone: ')
        pessoa['curso'] = input('Curso: ').upper()
        cadastro.append(pessoa)

    elif op == 2:
        if not cadastro:
            print('Nenhum cadastro efetuado!')
            continue
        else:
            frase = 'Lista de Inscritos'
            print('*' * len(frase))
            print(frase)
            print('*' * len(frase))
            for i in cadastro:
                print(f"Voucher: {i['voucher']}\nNome: {i['nome']}\nE-mail: {i['email']}\nTelefone: {i['telefone']}\nCurso: {i['curso']}", end="\n")
                print("-*-" * 20)

            sair = input('Deseja sair?\nS-sim  N-não: ').upper()

            if (sair == 'S'):
                print('Encerrando o programa...')
                sleep(1)
                print('Programa encerrado com sucesso.')
                break  # encerramento do looping.
            else:
                continue  # Dando continuidade ao looping.
    else:
        print('Encerrando o programa...')
        print()
        sleep(1)
        print('Programa encerrado com sucesso.')
        break
