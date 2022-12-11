columna = int(input())
fila = int(input())
columna2 = int(input())
fila2 = int(input())

# Si estan en la misma columna o fila
if columna == columna2 or fila == fila2:
    print("YES")
# Si estan en diagonal
elif abs(columna - columna2) == abs(fila - fila2):
    print("YES")
else:
    print("NO")
