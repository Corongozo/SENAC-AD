# 3. Rendimento do Taxista: 
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o 
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do 
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de 
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a 
# média do consumo em km/L e o lucro (líquido) do dia.  
# Preço do combustível
try:
    preco_combustivel = 6.15

    # Entrada de dados
    inicio_km = float(input("Digite a marcação do odômetro no início do dia (km): "))
    fim_km = float(input("Digite a marcação do odômetro no final do dia (km): "))
    litros_gastos = float(input("Digite o número de litros de combustível gastos: "))
    valor_recebido = float(input("Digite o valor total recebido dos passageiros (R$): "))

    # Cálculo da distância percorrida
    distancia = fim_km - inicio_km

    # Cálculo da média de consumo (km por litro)
    media_consumo = distancia / litros_gastos

    # Cálculo do gasto com combustível
    gasto_combustivel = litros_gastos * preco_combustivel

    # Cálculo do lucro líquido
    lucro = valor_recebido - gasto_combustivel

    # Saída dos resultados
    print("Média de consumo:", round(media_consumo, 2), "km/L")
    print("Lucro líquido do dia: R$", round(lucro, 2))
except ValueError:
    print('Imprima um valor válido.')
