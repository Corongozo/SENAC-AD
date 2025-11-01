# 6. Positivo ou Negativo: 
# Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o 
# valor zero como positivo. 
try:
    valor=float(input('Imprima um valor: '))
    if valor < 0:
        print('Valor negativo')
    else:
        print('Valor positivo')
except ValueError:
    print('Imprima um valor válido.')