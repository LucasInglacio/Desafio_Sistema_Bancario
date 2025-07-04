# Implementação do novo sistema para banco
menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor do depósito: ")) # Deposito do usuario

        if valor > 0:
            saldo += valor # sendo maior que 0, ele adiciona no saldo
            extrato += f"Depósito: R$ {valor:.2f}\n" # Concatena o valor da string ( formata em forma de dinheiro)

        else:
            print("Operação falhou! O valor informado é inválido.") # deposito negativo

    elif opcao == "1":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 # Faz a contagem de saque

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print("\n================ EXTRATO ================") #Cabecario (/n pula uma linha)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "3":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
