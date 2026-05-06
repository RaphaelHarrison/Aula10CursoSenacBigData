# Calcula média de notas
# Não sabemos quantos alunos, mas todos teraõ 4 notas sempre
def calcula_media(a):
    tot = sum(a)
    media = tot / len(a)
    return tot, media



contador = 1
resposta = "S"
while True:
    print(f"Aluno {contador}")
    contador += 1
    aluno = input("Nome do aluno: ")
    
    notas = []
    try:
        for i in range(4):
            nota = float(input("Informe a nota: "))
            notas.append(nota)
    except ValueError:
        print("Erro! Informe apenas valores válidos.")
    
    else:
        total, media = calcula_media(notas)

        print("\nResultado")
        print(f"Aluno: {aluno}")
        print(f"Total de Pontos: {total}")
        print(f"Média: {media:.2f}")
        
    finally:
        print("Processo encerraod para o aluno")
    
    
    resposta = input("Quer continuar(S/N)?").upper().strip()
    if resposta != "S":
        break