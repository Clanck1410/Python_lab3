# Создание списка и кортежа из 6 одинаковых значений
lst = [10, 20, 30, 40, 50, 60]
tpl = (10, 20, 30, 40, 50, 60)

print(f"Список: {lst}, тип: {type(lst)}, id: {id(lst)}")
print(f"Кортеж: {tpl}, тип: {type(tpl)}, id: {id(tpl)}\n")

# Изменение элемента списка
id_lst_before = id(lst)
lst[2] = 70
id_lst_after = id(lst)

print(f"Список после изменения: {lst}")
print(f"id до: {id_lst_before}, id после: {id_lst_after}, совпадает: {id_lst_before == id_lst_after}\n")

# Формирование нового кортежа с измененным элементом
id_tpl_before = id(tpl)
tpl_new = (tpl[0], tpl[1], 70, tpl[3], tpl[4], tpl[5])
id_tpl_after = id(tpl_new)

print(f"Новый кортеж: {tpl_new}")
print(f"id старого: {id_tpl_before}, id нового: {id_tpl_after}, совпадает: {id_tpl_before == id_tpl_after}")
