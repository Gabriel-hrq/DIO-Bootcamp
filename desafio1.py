menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.00
limite = 500.00
extrato = ''
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Digite um valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito feito no valor de {valor}\n'
            extrato += f'Saldo atual {saldo} \n##########################################\n'
        else:
            print('Valor inválido, digite um valor positivo.')

    elif opcao == 's':
        valor = float(input("Digite um valor para saque: "))
        if valor < 0.00:
            print("Valor inválido")
        elif valor > 0.00:
            if valor < limite and limite_saques <= 3:
                if saldo > valor:
                    saldo -= valor
                    numero_saques +=1
                    extrato += f'Saque feito no valor de {valor}\n'
                    extrato += f'Saldo atual {saldo} \n##########################################\n'
                    print("Saque realizado com sucesso!")
                elif saldo < valor:
                    print("Saldo insuficiente.")
                else:
                    if saldo == 0:
                        print("Saldo insuficiente.")
        else:
            print(f"Valor igual a {valor} nenhuma operação foi feita!")     
    elif opcao == 'e':
        print(extrato)

    elif opcao == 'q':
        break

    else:
        print("Opção inválida. ")