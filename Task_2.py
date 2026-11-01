# Список из 10 значений с явными повторами
lst = [1, 67, 42, 1, 12, 42, 12, 24, 20, 17]

# Преобразование во множество
unique_lst = set(lst)

print(f"Исходный список ({len(lst)} элементов):")
print(lst)
print(f"\nПолученное множество ({len(unique_lst)} элементов):")
print(unique_lst)
print(f"\nКоличество удаленных дубликатов: {len(lst) - len(unique_lst)}")
