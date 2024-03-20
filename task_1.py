import time   
import csv

def quickSort(s):
    if len(s) > 1:
        pivot = s.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in s:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
    else:
        return s

with open('scientist.txt', encoding='utf-8') as file:
    s = []
    f = list(file)[1:]
    for i in f:
        x = i.split('#')
        components = x[3]
        components = components[:-2]
        x[3] = components
        s.append(x)
    for el in s:
        time_list = el[2].split('-')
        time_string = time_list[0] + ', ' + time_list[1] + ', ' + time_list[2]
        result = time.strptime(time_string, "%Y, %m, %d")

with open('scientist_origin.txt', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerow(['ScientistName#preparation#date#components'])

        
    