numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index = 0
s = 0
ln = len(numbers)
for i in range(ln):
    if not numbers[i] is None:
        s += numbers[i]
    else:
        index = i
numbers[index] = s/ln
print("Измененный список:", numbers)
