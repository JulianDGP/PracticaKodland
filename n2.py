def es_vocal(letra):
    return letra in "aeiou"

def es_consonante(letra):
    return letra in "bcdfghjklmnpqrstvwxyz"

poema = ""
nLineas = int(input("How many lines will there be? "))
for i in range(nLineas):
    poema += "{0}\n".format(input().lower())
nConsonantes = 0
nVocales = 0
for letra in poema:
    if es_consonante(letra):
        nConsonantes += 1
    elif es_vocal(letra):
        nVocales += 1

#print(f"Number of vowels: {nVocales}\nNumber of consonants: {nConsonantes}")
print("Number of vowels: "+ str(nVocales)+ "\nNumber of consonants: "+ str(nConsonantes))
