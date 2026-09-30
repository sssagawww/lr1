import time

# Вариант 9

# Основные используемые escape-символы
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
RESET = '\u001b[0m'
START = '\u001b[1G'


# Рисование флага
def flag():
    # Параметры флага
    pixel = '  '
    length = 20
    height = 10
    for i in range(height):
        for j in range(length):
            # Если печатемый пиксель находится во второй трети по высоте \
            # или во второй шестой по длине, то печаем его синим, иначе - белмым
            if (height // 3 < i < 2 * (height // 3)) or \
                    ((length // 6) < j < 2 * (length // 6)):
                print(f'{BLUE}{pixel}{RESET}', end='')
            else:
                print(f'{WHITE}{pixel}{RESET}', end='')
        print()


# Анимация загрузки
def loading(tasks=3):
    bar_width = 25
    for n in range(tasks):
        for progress in range(1, bar_width + 1):
            bar = "#" * progress + "_" * (bar_width - progress)
            print(f'{START}Loading.. Task {n + 1}/{tasks} [{bar}] {progress * 4}%', end='', flush=True)
            time.sleep(0.1)
    print('\nDone!')


# Анимация с узором
def pattern(repeat=5):
    pixel = ' '
    size = 10
    # Повторим n раз кадры
    for n in range(repeat):
        # Узор - две окружности. Будем находить из уравнения окружности х и рисовать эту удвоенную величину.
        # Перебираем у от нижней координаты до верхней. Поставим шаг 2, чтобы сохранить размер узора size и сделать более круглым рисунок.
        for y in range(-size + 1, size, 2):
            paint_length = int((size ** 2 - y ** 2) ** 0.5)
            offset = size - paint_length
            print(f'{pixel * offset}\u001b[48;5;{10 + n}m{pixel * paint_length * 2}{RESET}'
                  f'{pixel * offset * 2}\u001b[48;5;{10 + n}m{pixel * paint_length * 2}{RESET}')
        # Возвращаем курсор наверх
        print(f'\u001b[{size + 1}A')
        # os.system('clear')
        time.sleep(2)


# Диаграмма процентного соотношения
def sequence():
    file = open('sequence.txt', 'r')
    nums = []
    negative_nums = []
    for line in file:
        # Распределяем числа по условию
        if 5 < float(line) < 10:
            nums.append(float(line))
        elif -10 < float(line) < -5:
            negative_nums.append(float(line))
    print(f'числа от 5 до 10:  {BLUE}{' ' * (len(nums) // 5)}{RESET}'
          f'{(len(nums) * 100 / (len(nums) + len(negative_nums))):.2f}%')
    print(f'исла от -10 до -5: {WHITE}{' ' * (len(negative_nums) // 5)}{RESET}'
          f'{(len(negative_nums) * 100 / (len(nums) + len(negative_nums))):.2f}%')
    file.close()


# Функция
def function():
    size = 24  # Размер графика (количество "клеток")
    graph_draw = ''  # Представим график в виде строки
    pixel = '  '
    for y in range(size, -1, -1):
        # y = x/2 => x = 2y
        x = 2 * y
        # Если полученный х поподает в размер графика, то пиксель, отвечающий за его у, будем рисовать синим
        if x < size:
            # Отметим значение на оси ОУ
            graph_draw += f' {y / 10}'
            # Между пикселями добавим 3 пробела (размер записи дробного числа), чтобы они были ровно над числами на ОХ
            graph_draw += f'{(pixel + '   ') * x}{BLUE}{pixel}{RESET}\n'
    # Отметим значение на оси ОХ, сделав отступ на 3 пробела (размер записи дробного числа)
    graph_draw += '   ' + pixel.join(map(str, [x / 10 for x in range(size + 1)]))
    print(graph_draw)


# flag()
# loading()
# pattern()
# sequence()
# function()

# os.system("cls") - IDE идентифицирует как устаревший софт - ?
