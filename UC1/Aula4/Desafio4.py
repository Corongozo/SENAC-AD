# 4. Código de Origem do Produto: 
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região 
# de sua procedência, conforme a tabela abaixo: 

# Observação: caso o código não seja nenhum dos especificados, o produto deve ser 
# encarado como “Importado”
try:
    # Entrada do código de origem
    codigo = int(input("Digite o código de origem do produto: "))

    # Verificação da região conforme a tabela
    match codigo:
        case 1:
            print("Região: Sul")
        case 2:
            print("Região: Norte")
        case 3:
            print("Região: Leste")
        case 4:
            print("Região: Oeste")
        case 5 | 6:
            print("Região: Nordeste")
        case n if 7 <= n <= 9:
            print("Região: Sudeste")
        case 10:
            print("Região: Centro-Oeste")
        case 11:
            print("Região: Noroeste")
        case _:
            print("Região: Importado")
except ValueError:
    print("Insira um valor válido.")