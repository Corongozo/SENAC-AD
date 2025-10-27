# Sistema de ordenação de numeros
num1=float(input('Primeiro valor: '))
num2=float(input('Segundo valor: '))
num3=float(input('Terceiro valor: '))

if num1<num2 and num1<num3:
    slot1=num1
elif num1>num2 and num1<num3:
    slot2=num1
    slot1=num2
    slot3=num3
elif num1<num2 and num1>num3:
    slot2=num1
    slot1=num3
    slot3=num2
elif num1>num2 and num1>num3:
    slot3=num1

if num2<num1 and num2<num3:
    slot1=num2
elif num2>num1 and num2<num3:
    slot2=num2
    slot1=num1
    slot3=num3
elif num2<num1 and num2>num3:
    slot2=num2
    slot1=num3
    slot3=num1
elif num2>num1 and num2>num3:
    slot3=num2

if num3<num1 and num3<num2:
    slot1=num3
elif num3>num1 and num3<num2:
    slot2=num3
    slot1=num1
    slot3=num2
elif num3<num1 and num3>num2:
    slot2=num3
    slot1=num2
    slot3=num1
elif num3>num1 and num3>num2:
    slot3=num3

print('Numeros em ordem:',slot1, slot2, slot3)