# TODO Напишите функцию find_common_participants
def find_common_participants (str1, str2, sep = ','):
    list1 = str1.split(sep)
    list2 = str2.split(sep)
    same_names = list()
    for name in list1:
        if name in list2:
            same_names.append(name)
    return sorted(same_names)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
sep = '|'
print(find_common_participants(participants_first_group, participants_second_group, sep))