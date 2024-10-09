# currency exchange

#pesos
a = int(input('What do you have left in pesos?'))
#soles
b = int(input('What do you have left in soles?'))
#reais
c = int(input('What do you have left in reais?'))

#conversion rates
pesos = (a * .00024)
soles = (b * .27)
reais = (c * .18)
total = ([pesos + soles + reais])

#printed answer
(print(total))
