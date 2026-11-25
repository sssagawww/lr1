from itertools import combinations


# Создание таблицы для динамического программирования
def get_table(n, cur_capacity, cur_items):
    dp = [[0 for _ in range(cur_capacity + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(cur_capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif cur_items[i - 1][1] <= j:
                dp[i][j] = max(cur_items[i - 1][2] + dp[i - 1][j - cur_items[i - 1][1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp


# Выбор предметов по созданной таблице
def get_backpack(n, cur_capacity, cur_items):
    dp = get_table(n, cur_capacity, cur_items)
    max_value = dp[n][cur_capacity]
    c = cur_capacity
    items_list = []

    for i in range(n, 0, -1):
        if max_value <= 0:
            break
        if max_value == dp[i - 1][c]:
            continue
        else:
            items_list.append(cur_items[i - 1])
            max_value -= cur_items[i - 1][2]
            c -= cur_items[i - 1][1]

    return items_list


def print_result(cur_capacity, cur_cols):
    # Добавляем антидот отдельно
    antidote = [item for item in items if item[0] == 'd'][0]
    other_items = [item for item in items if item[0] != 'd']
    cur_capacity -= antidote[1]

    # Собираем рюкзак и находим итоговые очки
    backpack = get_backpack(len(other_items), cur_capacity, other_items)
    backpack.append(antidote)
    total_value = sum(int(item[2]) for item in items)
    selected_value = sum(item[2] for item in backpack)
    points = 20 + 2 * selected_value - total_value

    # Печатаем инвентарь
    inventory = []
    for bp in backpack:
        inventory += [f'[{bp[0]}]'] * bp[1]
    for i in range(len(inventory)):
        print(inventory[i], '', end='')
        if i == cur_cols - 1:
            print()

    print('\nИтоговые очки выживания: ', points)


items = [('r', 3, 25),
         ('p', 2, 15),
         ('a', 2, 15),
         ('m', 2, 20),
         ('i', 1, 5),
         ('k', 1, 15),
         ('x', 3, 20),
         ('t', 1, 25),
         ('f', 1, 15),
         ('d', 1, 10),
         ('s', 2, 20),
         ('c', 2, 20)]

rows = 2
cols = 4
capacity = rows * cols
print_result(capacity, cols)

# Если 7 ячеек
capacity = 7
print_result(capacity, cols)

# Поиск положительных комбинаций
capacity = 8
total_value = sum(int(item[2]) for item in items)

for n in range(1, len(items) + 1):
    for c in combinations(items, n):
        size = sum(int(item[1]) for item in c)
        value = sum(int(item[2]) for item in c)
        has_antidote = any(item[0] == 'd' for item in c)
        points = 20 + 2 * value - total_value

        if size <= capacity and has_antidote and points > 0:
            names = [item[0] for item in c]
            print(names, "Очки:", points)
