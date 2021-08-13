# Exercício_1
lista = [5, 7, 2, 9, 4, 1, 3]
#1A
def total_elementos(list):
    count = 0
    for element in list:
        count += 1
    return count
print("Total da lista: ", total_elementos(lista))

#1B
prim = 5
seg = 7
terc = 2
quart = 9
quint = 4
sext = 1
set = 3
maior = prim
if (seg > maior):
    maior = seg
if (terc > maior):
    maior = terc
if (quart > maior):
    maior = quart
if (quint > maior):
    maior = quint
if (sext > maior):
    maior = sext
if (set > maior):
    maior = set
print("O maior elemento da lista é: ", maior) #B

#1C
prim = 5
seg = 7
terc = 2
quart = 9
quint = 4
sext = 1
set = 3
menor = prim
if (seg < menor):
    menor = seg
if (terc < menor):
    menor = terc
if (quart < menor):
    menor = quart
if (quint < menor):
    menor = quint
if (sext < menor):
    menor = sext
if (set < menor):
    menor = set
print("O menor elemento da lista é: ", menor)

#1D
soma = 0
for i in lista:
   soma += i
print("A soma dos elementos da lista é: ", soma)


#1E
primeiro = 5
segundo = 7
terceiro = 2
quarto = 9
quinto = 4
sexto = 1
setimo = 3
if sexto<terceiro<setimo<quinto<primeiro<segundo<quarto:
	print("Lista em ordem crescente: ",sexto,terceiro,setimo,quinto,primeiro,segundo,quarto)

#1F
if quarto>segundo>primeiro>quinto>setimo>terceiro>sexto:
	print("Lista em ordem decrescente: ",quarto,segundo,primeiro,quinto,setimo,terceiro,sexto)




