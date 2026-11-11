from string import ascii_uppercase
from random import sample, choices
import tkinter as tk
import pygame

field_x = 720 / 2


# Анимация движения поля в правой половине экрана
def move_field_right():
    global field_x
    if field_x <= 720 * 2:
        field_x += 20
        key_label.place(x=field_x, y=(480 / 2), anchor='center')
        window.after(5, move_field_right)
    else:
        field_x = -720 / 2
        key_label.place(x=field_x, y=(480 / 2), anchor='center')
        move_field_left()


# Анимация движения поля в левой половине экрана
def move_field_left():
    global field_x
    if field_x < (720 / 2):
        field_x += 20
        key_label.place(x=field_x, y=(480 / 2), anchor='center')
        window.after(5, move_field_left)
    else:
        key_label.place(x=field_x, y=(480 / 2), anchor='center')


# Генерация ключа
def generate_key():
    alph = ascii_uppercase
    nums = list(range(1, 27))
    borders = sorted(sample(nums, 2))
    left_b = borders[0]
    right_b = borders[1]
    mid_section = ''.join(choices(alph[left_b - 1:right_b], k=7))
    key = str(f'{str(left_b).zfill(2)} {mid_section} {str(right_b).zfill(2)}')
    key_label.configure(text=key)
    move_field_right()


# Создание окна
window = tk.Tk()
window.title('Генератор ключей')
window.geometry('720x480')

# Установка фона
bg_img = tk.PhotoImage(file='mc.png')
bg_img = bg_img.subsample(3)
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# Заголовок
title_label = tk.Label(window, text='Ваш ключ:', font=("Arial Bold", 30))
title_label.pack(expand=True)

# Поле для ключа
key_label = tk.Label(window, text='Нажмите ниже', font=("Arial Bold", 40))
key_label.place(x=field_x, y=(480 / 2), anchor='center')

# Кнопка
btn = tk.Button(window, text='Сгенерировать', font=("Arial Bold", 20), command=generate_key)
btn.pack(expand=True)

# Включение музыки
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

window.mainloop()
