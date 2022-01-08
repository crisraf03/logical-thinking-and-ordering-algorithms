# %%
#algoritmos de ordenamiento 

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        k = 0
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                k +=1
                if k == 0:
                    return(array)
    print(array)
    
    
def selection_sort(array,show = False):
    for i in range(len(array)):
        index = i 
        for j in range(i+1, len(array)):
            if array[index] > array[j]:
                index = j
        
        array[i], array[index]  = array[index], array[i]
    print("el arreglo ordenado es:" + str(array))

# %%
bubbleSort(arr_1)
selection_sort(arr_2, True)

# %%
def orden_1(x):
    y = x[:]
    box = []
    j = 0
    it = 0
    while j < len(y):
        if y[j] == min(y):
            box.append(y[j])
            y.remove(y[j])
            j = 0
        else:
            j += 1
        it += 1
#         print(len(y), j ,y, box)
    return(it, box)

# %%
arr_1 = [3,6,76,4,93,11,143,12,65,44,23,56,887,223,343]
arr_2 = [3,4,64,2,45,75,24,565]

print(orden_1(arr_1))        

# %%
import random
import numpy as np


def eficiencia(x): #x es el largo de las listas 
    y = np.zeros(10)
    for j in range(10):
        A = []
        for u in range(x):
            num = random.randint(0,100)
            A.append(num)
        y[j] += orden_1(A)[0]
    return(np.mean(y))
    
# eficiencia(10), eficiencia(100) , eficiencia(1000) =  33.1, 2577.5,  247878.7
# diviendiendo y redondeando 3, 26, 250, ... o si se quiere 2.5 , 25 , 250 ...


