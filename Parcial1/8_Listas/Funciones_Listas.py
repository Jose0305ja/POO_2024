paises=["Mexico", "USA", "Brasil", "China"]
numeros=[100,80,3.1416,75]
varios=["UTD", True, 100,0.100]

paises.sort()
print (paises)

numeros.sort()
print (numeros)

#Esto siguiente no se puede ya que necesitan ser del mismo tipo
# varios.sort()
# print (varios)


#Agregar elemento
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)

#Remover elementos
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros)

#Dar la vuelta a los elementos 
varios.reverse()
print (varios)

#Buscar un valor o dato dentro de una lista
encontro="Brasil" in varios
print (encontro)

#Vaciar una lista
print(paises)
paises.clear()
print(paises)

#Unir listas
print(varios)
varios.extend(numeros)
print (varios)