print(" === Cálculo de Produtividade === ")

try:
    total_produzido = float(input("Valor total da venda: "))
    funcionarios = int(input("Total de Funcionários: "))

    media_por_funcionario = total_produzido / funcionarios
    
except Exception as e:
    print(f"Ops! Erro nos valores de entrada: {e}")
except KeyboardInterrupt:
    print("Operação encerrada.")

else:
    print(f"Média por funcionário: {media_por_funcionario:.2f}")
    
finally:
    print("Programa Encerrado")