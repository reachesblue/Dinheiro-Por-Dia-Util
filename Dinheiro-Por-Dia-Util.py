"""
Thanks everyone
My GitHub: https://github.com/reachesblue
"""

import time

def calcular_primeiro_ano():
    dinheiro1 = int(input('Quanto de dinheiro deseja calcular: '))
    todo = dinheiro1 * 254
    print('')
    print(f'O total de dinheiro que você terá em 1 ano será de {todo}')
    time.sleep(6)
    print("\n" * 130)


def calcular_mais_um_ano():
    pergunta6 = input('Gostaria de multiplicar por mais de 1 ano (sim ou nao): ')
    print("\n" * 130)
    while pergunta6 == 'sim':
        dinheiro4 = int(input('Quanto de dinheiro deseja calcular: '))
        pergunta2 = int(input('Por quantos anos gostaria de multiplicar: '))
        var = 254 * pergunta2
        var2 = dinheiro4 * var
        print('')
        print(f'Em {pergunta2} anos você terá um total de {var2} reais')
        time.sleep(3)
        print('')
        pergunta6 = input('Gostaria de multiplicar de novo (sim ou nao): ')
    else:
        print('Ok, obrigado por usar o programa :)')


def calcular_por_mes():
    print("\n" * 130)
    quest2 = input('Gostaria de fazer o calculo mensal (sim ou nao): ')
    while quest2 == 'sim':
        print('Lembrando que depende do mes, pois cada mês tem festas diferentes')
        dinheiro4 = int(input('Quanto de dinheiro deseja calcular: '))
        pergunta2 = int(input('Por quantos meses gostaria de multiplicar: '))
        var = 21 * pergunta2
        var2 = dinheiro4 * var
        print('')
        print(f'Em {pergunta2} meses você terá um total de {var2} reais')
        time.sleep(3)
        print('')
        quest2 = input('Gostaria de multiplicar de novo (sim ou nao): ')
    else:
        print('Ok, obrigado por usar o programa :)')


def creditos():
    print('Programa feito por: Riique')
    print('Muito obrigado por ter usa-lo!')
    print('Programa feito na linguagem Python!')
    print('')
    print('Meu discord: Riique#0001')
    print('')
    print('Programa fechando em 20 segundos! Muito obrigado :)')
    time.sleep(20)


def iniciar():
    print('Contador De Dinheiro!     V.0.0.2')
    print('')
    print('')
    print('Olá seja bem vindo ao programa que calcula o quanto você economiza por DIA UTIL')
    print('Todas as contas feitas serão por dia util')
    print('')
    print('[1] - Calcular apenas 1 ano')
    print('[2] - Calcular mais de 1 ano')
    print('[3] - Calcular por mes')
    print('[4] - Creditos do programa')
    print('')
    escolha = int(input('Escolha o que deseja pelos numeros: '))
    if escolha == 1:
        print("\n" * 130)
        calcular_primeiro_ano()
    elif escolha == 2:
        print("\n" * 130)
        calcular_mais_um_ano()
    elif escolha == 3:
        print("\n" * 130)
        calcular_por_mes()
    elif escolha == 4:
        print("\n" * 130)
        creditos()
    else:
        print('Você não digitou nada!')
        print('')
        print('Saindo!')
        print('')

iniciar()