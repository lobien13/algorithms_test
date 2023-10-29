#Elementos tienene que estar ordenados

arr =[2,4,1,3,5,9,7,8,6]

def sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

sort(arr)
print(arr)

def busquedabinaria(arr, x):
    min = 0
    max = len(arr)-1
    mid = 0
    while min <= max:
        mid = (max + min) // 2
        if arr[mid] < x:
            min = mid + 1
        elif arr[mid] > x:
            max = mid- 1
        else:
            return mid
    return -1

resultado = busquedabinaria(arr, 4)
if resultado != -1:
    print(f"El elemento 4 se encuentra en la posición {resultado}")
else:
    print("El elemento 4 no se encuentra en la lista.")


