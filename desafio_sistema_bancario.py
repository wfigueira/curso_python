## Sacar, depositar e extrato
opcao = -1
menu = '''
#######################
    Qual operacao deseja realizar?
    [1] - Deposito
    [2] - Saque
    [3] - Extrato
    [0] - Sair
######################
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while opcao != 0:
    
    print(menu)
    opcao = int(input("Digite a sua escoha: "))    
    
    if opcao == 1:
        print("Deposito")
        valor_deposito = float(input("Digite o valor que gostaria de depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"

        else:
            print("Operação falhou: O valor informado é inválido")
    
    elif opcao == 2:
        print("saque")
                
        valor_saque = float(input("Digite o valor que gostaria de sacar: "))

        excedeu_saque = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saque:
            print("Operação falhou! Você não tem saldo suficiente")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedr o limite")
        
        elif excedeu_saques:
            print("Operação falhou! Numero máxido de saques excedido")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else:
            print("OOperação falhou! O valor informado é inválido")

    elif opcao == 3:
        print("\n=============== Extrato ======================")
        print ("Não foram realizdas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===============================================")

    elif opcao == 0:
        break
    else:
        print ("Opcao invalida")

else:
    print("Obrigado por usar nosso sistema bancário, até logo")   