# 1. Cálculo de Média Escolar para Vários Alunos 
# Use o laço for para repetir a lógica de cálculo de média e status 
# (Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.
for i in range(10):
    try:
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

        # Verificação da situação do estudante
        print("Média do semestre:", round(media, 2))

        if media >= 6.0:
            print("Situação: Aprovado")
        elif media < 3.0:
            print("Situação: Reprovado")
        else:
            print("Situação: Recuperação")
    except ValueError:
        print("Valor invalido.")
