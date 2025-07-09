menu = """
========== Opções ==========
[1] Depositar              
[2] Sacar                  
[3] Extrato                
[4] Sair                   
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Qual valor você deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("O valor informado é inválido.")

    elif opcao == 2:
        valor = float(input("Qual valor você deseja sacar: "))

        if numero_saques >= limite_saques:
            print("Você só pode realizar 3 saques por dia.")

        elif valor < 0:
            print("O valor informado é inválido.")

        elif valor > saldo:
            print("Saldo insuficiente.")

        elif valor > limite:
            print("O valor excedeu o limite.")
            
        else:
            numero_saques += 1

            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"

    elif opcao == 3:
        print("========== Extrato ==========")
        print("Sem movimentações na conta." if extrato == "" else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=============================")

    elif opcao == 4:
        break

    else:
        print("Operação inválida! Selecione novamente a opção desejada.")