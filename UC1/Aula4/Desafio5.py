# 5. Média do Aluno com Optativa: 
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação 
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve 
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa 
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e 
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em 
# recuperação, de acordo com as informações abaixo:  
# Aprovado: média >= 6.0 
# Reprovado: média < 3.0 
# Recuperação: média >= 3.0 e < 6.0 
# Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o 
# resultado final.
# Entrada das notas
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