i = input("Введите кол-во элементов:")

li = []
for j in range(1, int(i)+1) :
    inp = "Введите " + str(j) + " элемент:"
    k = input(inp)
    li.append(k)

print("Вывод:", li)