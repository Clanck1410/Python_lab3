# Кортеж: неизменяемые сведения о мероприятии
conf_info = ("Программирование вычислительных систем", "14.10.2026", "Главный корпус, аудитория 209")

# Список: порядок поступления заявок
applications_order = [201, 205, 212, 219, 224, 230]

# Множество: уникальные идентификаторы уже зарегистрированных участников
registered_ids = {201, 205, 212, 219, 224, 230}

# Словарь: связь id_участника -> ФИО
participants = {
    201: "Соколов Артем Дмитриевич",
    205: "Морозова Полина Игоревна",
    212: "Волков Максим Сергеевич",
    219: "Кузнецова Дарья Андреевна",
    224: "Лебедев Никита Павлович",
    230: "Купцова Алиса Романовна"
}

# Вывод исходного состояния
print(f"Параметры конференции: «{conf_info[0]}», {conf_info[1]}, {conf_info[2]}")
print(f"Заявки в порядке поступления: {', '.join(map(str, applications_order))}")
print(f"Зарегистрированные участники: {', '.join(map(str, sorted(registered_ids)))}")
print("Участники:")
for uid, name in participants.items():
    print(f"  {uid} — {name}")

# Добавление новой заявки в список
new_applicant = 245
applications_order.append(new_applicant)
print(f"\nПосле добавления заявки: {', '.join(map(str, applications_order))}")

# Проверка наличия заданного идентификатора среди зарегистрированных
check_id = 212
is_registered = "да" if check_id in registered_ids else "нет"
print(f"Участник {check_id} зарегистрирован: {is_registered}")

# Получение ФИО участника по идентификатору
target_id = 205
target_name = participants.get(target_id, "Участник не найден")
print(f"ФИО участника {target_id}: {target_name}")
