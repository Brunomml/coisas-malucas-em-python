#importando a nossa forma de escolher a pizza
from random import randint

#lista de pizza
lista_de_pizza = ["calabreza", "frango", "mussarela", "presunto", "alho", "toscana", "portuguesa", "champignom", "4 queijo"]

#randomizando as pizzas
escolha_de_pizza = randint(0,8)

#mostrando o resutado
print("a pizza escolhida foi", lista_de_pizza[escolha_de_pizza])
