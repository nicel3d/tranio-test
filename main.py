#! /usr/bin/python python
data = [13, 29, 37, 49, 29, 7, 25, 5, 50, 2, 18, 0, 14, 16, 14, 4, 6, 14, 2, 5, 41, 27, 10, 11, 33, 6, 7, 47, 35,
        35, 48, 0, 38, 1, 41, 15, 26, 46, 4, 23, 5, 32, 45, 37, 2, 33, 20, 30, 46, 20, 10, 14, 44, 25, 3, 27, 6, 22,
        9, 20, 18, 43, 5, 33, 27, 41, 38, 20, 6, 2, 18, 29, 34, 40, 41, 8, 44, 30, 21, 10, 6, 1, 12, 0, 22, 28, 47,
        4, 5, 1, 11, 21, 1, 44, 24, 42, 42, 41, 14, 24]

def only(data):
    arr = []
    for i in data:
        if i not in arr:
            arr.append(i)
    return arr

def notNumberList(data, moreNumber = 40):
    arr = []
    newarr = []
    for i in data:
        if int(i) <= 40:
            if i not in arr:
                arr.append(i)
    i = 0
    while i <= moreNumber:
        if i not in arr:
            newarr.append(i)
        i=i+1
    return [arr, newarr]

def sort_col(i):
    return i[n]

def countNumberText(data):
    arr = []
    newarr = [[]*2]*len(data)
    data.sort()
    for i in data:
        if i not in arr:
            arr.append(i)
            newarr.insert(i, [i, 1])
        elif newarr[i]:
            txt = newarr[i][1] + 1
            newarr[i] = [i, txt]
    newarr = list(filter(None, newarr))
    newarr.sort(key=lambda i:i[1])
    return newarr

def avgQudraticValues(data):
    n = int(len(data))
    qi = 0
    summ = 0
    for i in data:
        summ = summ + i
    summ = summ / n

    for i in data:
        qi = qi + pow(i - summ, 2)
    summ = qi / n
    return round(summ, 2)

print("\n1. Вывести список уникальных чисел (встречаются только один раз):")
print(only(data))

print("\n2. Вывести список чисел <= 40, не встречающихся в исходном списке:")
text = notNumberList(data)
print("исходный:\t\t" + str(text[0]))
print("не встречаются:\t" + str(text[1]))

print("\n3. Вывести данные в формате \n\
(num: num_count), \n\
(num: num_count),\n\
 ... \n\
num_count - кол-во num в списке. \n"
      + "Отсортировать по убыванию num_count, \n"
      + "при равенстве num_count по убыванию num.")
array = countNumberText(data)
print("num\t:\tnum_count")
for i in array:
    print(str(i[0]) + "\t:\t" + str(i[1]))

print("4. Рассчитать среднеквадратичное отклонение:")
print(avgQudraticValues(data))