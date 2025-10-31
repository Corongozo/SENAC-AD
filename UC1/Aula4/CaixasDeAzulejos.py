# 2. Quantidade de Caixas de Azulejos: 
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, 
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em 
# todas as suas paredes (considere que não será descontada a área ocupada por portas e 
# janelas). Cada caixa de azulejos possui 1,5 m²
# Entrada de dados
try:
    comprimento = float(input("Digite o comprimento da cozinha: "))
    largura = float(input("Digite a largura da cozinha: "))
    altura = float(input("Digite a altura da cozinha: "))

    area_paredes = 2 * altura * (comprimento + largura)

    caixas = area_paredes / 1.5

    if caixas != int(caixas):
        caixas = int(caixas) + 1
    else:
        caixas = int(caixas)

    # Saída
    print(f"Você precisará de {caixas} caixa(s) de azulejos para revestir todas as paredes.")
except ValueError:
    print("Porfavor, insira uma valor válido.")