#Sistema de status de estudante
nota1=float(input('Primeiro valor: '))
nota2=float(input('Segundo valor: '))
nota3=float(input('Terceiro valor: '))
nota4=float(input('Quarto valor: '))

media=(nota1+nota2+nota3+nota4)/4
print('Sua média é ', media)
if media<5:
    print('Você esta reprovado!!')
elif media>=5 and media<=7:
    print('Vai para a recuperação!!')
elif media>7:
    print('Você foi aprovado!!')
else:
    print('Erro de digitação')