menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Quanto você deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"entrada: R$ {deposito}\n"
        
        else:
            print("Não foi possival realizar seu deposito!")

    elif opcao == "s":
        saque = float(input("Quanto você deseja sacar: "))

        if saque > limite:
            print("Não foi possival realizar seu saque, pois o valor exede o limite de R$ 500.")

        elif saque > saldo:
            print("Não foi possival realizar seu saque, pois você não possui fundo suficiente.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Não foi possival realizar seu saque, pois você atingiu seu limite diario de saques.")

        elif saque > 0:
            saldo -= saque
            extrato += f"saida: R$ {saque}\n"
            numero_saques += 1

        else:
            print("Não foi possival realizar seu saque!")

    elif opcao == "e":
        cabecalho = "Extrato"
        
        print(cabecalho.center(40,"#"))
        print(extrato)
        print("".center(40, "#"))
        print(f"Seu saldo é de: R$ {saldo}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
