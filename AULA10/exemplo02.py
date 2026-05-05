#Este for é para executar quando há um erro
# for i in range(5):
#     total_produzido = float(input("Valor total da venda: "))
#     funcionarios = int(input("Total de Funcionários: "))

#     media_por_funcionario = total_produzido / funcionarios
#     print(f"Média por funcionário: {media_por_funcionario:.2f}")


# for ocm try: não par de executar, caso lance um erro
for i in range(5):
    try:
        total_produzido = float(input("Valor total da venda: "))
        funcionarios = int(input("Total de Funcionários: "))

        media_por_funcionario = total_produzido / funcionarios
        print(f"Média por funcionário: {media_por_funcionario:.2f}")
    except ValueError:
        print("Favor informar um número.")
    except ZeroDivisionError:
        print("Funcionário não pode ser Zero.")