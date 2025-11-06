# Média Escolar para 5 Estudantes 
# Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão 
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma 
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().
resultado = []
for i in range(2):
    try:
        print('-'*90,)
        print(f'Aluno {i+1}:')
        nota1 = float(input("Digite a nota da primeira avaliação: "))
        nota2 = float(input("Digite a nota da segunda avaliação: "))
        optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

        # Substituição da menor nota, se a optativa foi feita
        if optativa != -1:
            if nota1 < nota2:
                nota1 = optativa
            else:
                nota2 = optativa

        # Cálculo da média
        media = (nota1 + nota2) / 2

        if media >= 6.0:
            resultado.append(f"Aluno {i+1} Situação: Aprovado")
        elif media < 3.0:
            resultado.append(f"Aluno {i+1} Situação: Reprovado")
        else:
            resultado.append(f"Aluno {i+1} Situação: Recuperação")
    except ValueError:
        print("Valor invalido.")
for i in resultado:
    print('-'*90)
    print(i)
