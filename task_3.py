# Создайте словарь со списком вещей для похода
# в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

# список предметов
BAGGAGE = {
    'палатка': 10, 'спальник': 5, 'чайник': 0.5,
    'удочка': 0.2, 'вода': 5, 'еда': 7,
    'репеленты': 1, 'котелок': 0.7,
    'топорик': 1.5, 'спички': 0.1
}

# максимальная вместимость рюкзака
BACKPACK_CAPACITY = 20

def put_in_backpack(items: dict, max_weight: float) -> list:
    # сортировка вещей по весу от большего к меньшему
    sorted_items = sorted(items.items(), key=lambda x: -x[1])

    # создание списка для хранения выбранных вещей
    selected_items = []
    current_weight = 0

    for item, weight in sorted_items:
        if current_weight + weight <= max_weight:
            selected_items.append(item)
            current_weight += weight

    return selected_items

selected_baggage = put_in_backpack(BAGGAGE, BACKPACK_CAPACITY)

print(f'В рюкзак вместимостью {BACKPACK_CAPACITY}\
     поместится {selected_baggage}')