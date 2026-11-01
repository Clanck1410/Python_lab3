import sys

# Словарь: уникальный ID -> текстовое значение
users = {
    101: "Алексей",
    102: "Елена",
    103: "Дмитрий",
    104: "Мария",
    105: "Сергей"
}

# Доступ по известному ключу
user_id = 103
print(f"Поиск по ключу {user_id}: {users.get(user_id)}\n")

# Подготовка структур из 5 сопоставимых элементов
c_tuple = ("k1", "k2", "k3", "k4", "k5")
c_list  = ["k1", "k2", "k3", "k4", "k5"]
c_set   = {"k1", "k2", "k3", "k4", "k5"}
c_dict  = {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4", "k5": "v5"}

print("Размер структур в памяти (sys.getsizeof):")
print(f"Кортеж (tuple) : {sys.getsizeof(c_tuple)} байт")
print(f"Список (list)   : {sys.getsizeof(c_list)} байт")
print(f"Множество (set) : {sys.getsizeof(c_set)} байт")
print(f"Словарь (dict)  : {sys.getsizeof(c_dict)} байт")
