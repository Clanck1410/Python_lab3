import timeit

sizes = [1_000, 10_000, 100_000]
results = []

for n in sizes:
    lst_data = list(range(n))
    set_data = set(range(n))
    
    target_present = n - 1 # Худший случай для успешного поиска в списке (в самом конце)
    target_absent = -1 # Элемент гарантированно отсутствует
    
    repeats = 10_000
    
    # Замеры для списка
    t_lst_pres = timeit.timeit(lambda: target_present in lst_data, number=repeats)
    t_lst_abs = timeit.timeit(lambda: target_absent in lst_data, number=repeats)
    
    # Замеры для множества
    t_set_pres = timeit.timeit(lambda: target_present in set_data, number=repeats)
    t_set_abs = timeit.timeit(lambda: target_absent in set_data, number=repeats)
    
    results.append((n, t_lst_pres, t_lst_abs, t_set_pres, t_set_abs))

# Вывод результатов в виде таблицы
print(f"{'Размер (N)':<12} | {'List (есть), с':<15} | {'List (нет), с':<15} | {'Set (есть), с':<15} | {'Set (нет), с':<15}")
print("-" * 80)
for row in results:
    print(f"{row[0]:<12} | {row[1]:<15.5f} | {row[2]:<15.5f} | {row[3]:<15.5f} | {row[4]:<15.5f}")
