"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
"""
l = []

try:
    n = int(input('Enter number of elements: '))
    for i in range(n):
        el = input(f'Enter {i} element of list: ')
        l.append(el)
    
    print('Original l:', l)
    l1 = l[:-1:2] if len(l)%2 != 0 else l[::2]
    l2 = l[1::2]
    
    if len(l)%2 != 0: 
        l[1:-1:2] = l1
        l[:-1:2] = l2
    else: 
        l[1::2] = l1
        l[::2] = l2
    
    print('Changed l:', l)
except ValueError as ex:
    print(ex)