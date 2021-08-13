#Exercício_4
pergunta ='SIM'

while pergunta == 'SIM':
    quantidade= int(input('Qual a quantidade de linhas?'))
    print(':',quantidade*'-')
    pergunta=str(input('Quer continuar brincando?sim ou não?')).upper()