# 1. Cálculo de Lâmpadas: 
# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para 
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da 
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do 
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada 
# 3m² existe um bocal para uma lâmpada.

#Definição
potencia_lampada=float(input('Informe a potencia da lampada: '))
largura=float(input('Informe a largura do comodo: '))
comprimento=float(input('Informe a comprimento do comodo: '))

#Calculo
area=largura*comprimento
potencia_necessaria=area*3
bocais=area/3
lampadas_necessarias=potencia_necessaria/potencia_lampada

bocais=int(bocais) if bocais == int(bocais) else int(bocais) + 1

#a fazer