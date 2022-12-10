entrada = input("Ingrese una lista de numeros separados por espacios:")
lista = list(map(int, entrada.split()))
# print("Lista original: "+ str(lista))
i = 0
nCeros = 0;
while i < len(lista) - nCeros:
    if lista[i] == 0:
        lista.pop(i)
        lista.append(0)
        i -= 1
        nCeros += 1
    i += 1
# print("Lista Reducida: "+ str(lista))

for i in range(len(lista)):
    print(str(lista[i]), end=" ")
