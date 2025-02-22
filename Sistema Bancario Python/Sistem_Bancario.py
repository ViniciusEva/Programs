menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

limite_saque = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print('===========Depósito=============')
        valor =  float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nOperação Falha!\nDigite um numero positivo")
    
    elif opcao == "s":
        print("============Saque=============")
        if numero_saques == LIMITE_SAQUES:
            print("Você atingiu seu limite de saques, que são 3 tentativas!")
        elif limite_saque >= limite:
            print("Você atingiu seu limite de R$500,00")
        else:
            valor = float(input("Digite o Valor de Saque: "))
            if valor > 0 and valor <= saldo:
                saldo -= valor
                numero_saques +=1
                limite_saque += valor
                extrato += f"Saque: R$ {valor:.2f}\n"
            else:
                print("Digite um valor de saque disponivel")

    
    elif opcao == "e":
        print("===================Extrato========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print('==================================================')
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Selecione uma operação existente")