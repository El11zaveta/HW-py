#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input("Ввести число элементов в массиве: ")) 
ai = list(map(int, input().split()))
x = int(input("Ввести число Х: "))
b = ai[0] 
min = abs(x - b)  

for i in range(1, n):
    diff = abs(x - ai[0]) 
    if diff < min:  
        min = diff 
        b = ai[i] 
print(b)
