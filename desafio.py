menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        quantia = float(input("Digite a quantia a ser depositada: "))
        if quantia > 0:
            saldo += quantia
            extrato += f""" Deposito de R${quantia}   \n"""
            print(f'R${quantia:.2f} Depositado com sucesso \n')
        else:
            print("Não é possivel depositar valores negativos")

    elif opcao == 's':
        quantia = float(input("Digite a quantia a ser retirada: "))
        if quantia > 0:

            if numero_saques < LIMITE_SAQUES:
                if quantia <= LIMITE and saldo >= quantia:
                    saldo-=quantia
                    numero_saques+=1
                    extrato += f""" Saque de R${quantia} \n"""
                    print(f"R${quantia:.2f} retirada com sucesso")
                else:
                    print("Saldo insuficiente ou limite excedido")
            else:
                print("Limite de saques excedido..")
        else:
            print("Quantia a ser retirada não pode ser menor ou igual a 0")

    elif opcao == 'e':

        print(extrato + f"\n   Saldo: R${saldo:.2f}   ")

    elif opcao == 'q':
        print("Saindo")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada")