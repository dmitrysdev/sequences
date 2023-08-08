sl = input("Введите элементы списка через запятую:")
li = sl.split(",")
li2 = sl.split(";")
li3 = sl.split("/")
sep = ", "

if len(li) > 1 and len(li2) > 1:
    print("Можно использовать один из 3-х разделителей: запятую, точку с запятой, слэш")
    exit()
if len(li2) > 1 and len(li3) > 1:
    print("Можно использовать один из 3-х разделителей: запятую, точку с запятой, слэш")
    exit()
if len(li) > 1 and len(li3) > 1:
    print("Можно использовать один из 3-х разделителей: запятую, точку с запятой, слэш")
    exit()
if len(li2) > 1:
    li = li2
    sep = "; "
if len(li3) > 1:
    li = li3
    sep = "/ "

li.sort()
unique_numbers = set(li)
res = ''

for s in unique_numbers:
    if res :
        res = res + sep + s
    else:
        res = s

print("Результат:", res)
