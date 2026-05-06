# Simule um caixe eletrônico, o sistema deve iniciar com um saldo de 1000,00 e soliciar ao usuário o valor que deseja sacar
# apos tentativa de saque exibir mensagens informando o resultado da operação e finalize a operação mostrando o saldo que ficou

saldo = 1000.00
cond = True
while cond == True:
    print("========= Bem Vindo =========")
    print(f"Saldo: {saldo}")
    print("Quanto deseja sacar hoje?")
    try:
        saque = float(input("Valor: "))
        if saque == 0:
            cond = False
            print(f"Finalizando programa.")
        if saldo < saque:
            print("Valor do saque maior que o saldo. Tente novamente.\n")
        else:
            saldo = saldo - saque
            print(f"Saldo: {saldo:.2f}\n")
    except (ValueError, TypeError):
        print("Favor digitar um número!\n")
         