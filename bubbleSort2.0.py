arreglo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(str(len(arreglo)))
cont = 0
while(cont < len(arreglo)):
    definirArreglo = (input("Se ordenará un arreglo de 10 elementos de manera ascendente, con bubbleSort. Inserte el número en la posición " + str(cont) + " : "))
    arreglo[cont] = definirArreglo
    cont += 1

def bubbleSort(arr):
    print("Arreglo desordenado: "+ str(arr))
    n = len(arr)
    for i in range(n-1):
        ordenado = True
        for j in range(n-i): #Para evitar comparaciones innecesarias, se resta el length con el contador i.
            if(arr[j] > arr[j + 1]):
                ordenado = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if ordenado:
            break
    print("Arreglo ordenado: " + str(arr))

if __name__ == '__main__':
    bubbleSort(arreglo)