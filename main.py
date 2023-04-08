# -*- coding: utf-8 -*-

# # # # Copyright (C) 2023 Vladimir Zakharov
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # This file is part of average_score
#
# TranslatorVK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
#
# TranslatorVK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Скрипт создан с использованием графического интерфейса Tkinter
-----
Вы можете запустить код по ссылке https://replit.com/@WtoP4Ike/Progect2?v=1
Нажав кнопку зеленую run в верхнем правом углу
-----
"""
from tkinter import *
from tkinter import ttk
import random
def save_ps(txt):
  x = open('pass.txt','r+')
  x.seek(0)
  x.write(f'{txt}')
  x.close()
root = Tk()
root.title("Генерация пароля")
root.geometry("500x500")
label = ttk.Label(text="Символы и их количество:")
label.pack()
def gen():
  a=int(combobox.get())
  if eng.get() != 1 and ru.get() != 1 and ch.get() != 1:
    txt="Вы не выбрали символы."
  elif eng.get() == 1 and ru.get() != 1 and ch.get() != 1:
    chars = list('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(chars)
    par = ''.join([random.choice(chars) for x in range(a)])
    txt=par
    save_ps(txt)
  elif eng.get() == 1 and ru.get() == 1 and ch.get() != 1:
    chars = list('абвгдеёжзийклмнопрстуфхчцшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЦШЩЪЫЬЭЮЯabcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(chars)
    a=int(combobox.get())
    par = ''.join([random.choice(chars) for x in range(a)])
    txt=par
    save_ps(txt)
  elif eng.get() != 1 and ru.get() == 1 and ch.get() != 1:
    chars = list('абвгдеёжзийклмнопрстуфхчцшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЦШЩЪЫЬЭЮЯ')
    random.shuffle(chars)
    a=int(combobox.get())
    par = ''.join([random.choice(chars) for x in range(a)])
    txt=par
    save_ps(txt)
  elif eng.get() == 1 and ru.get() == 1 and ch.get() == 1:
    chars = list('+-/*!&$#?=w@<>абвгдеёжзийклмнопрстуфхчцшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЦШЩЪЫЬЭЮЯ1234567890abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(chars)
    a=int(combobox.get())
    par = ''.join([random.choice(chars) for x in range(a)])
    txt=par
    save_ps(txt)
  elif eng.get() != 1 and ru.get() != 1 and ch.get() == 1:
    chars = list('+-/*!&$#?=w@<>123456789')
    random.shuffle(chars)
    a=int(combobox.get())
    par = ''.join([random.choice(chars) for x in range(a)])
    txt=par
    save_ps(txt)
  elif eng.get() != 1 and ru.get() != 1 and ch.get() == 1:
    chars = list('+-/*!&$#?=w@<>абвгдеёжзийклмнопрстуфхчцшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЦШЩЪЫЬЭЮЯ1234567890')
    random.shuffle(chars)
    a=int(combobox.get())
    par = ''.join([random.choice(chars) for x in range(a)])
    txt=par
    save_ps(txt)
  elif eng.get() == 1 and ru.get() != 1 and ch.get() == 1:
    chars = list('+-/*!&$#?=w@<>1234567890abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(chars)
    a=int(combobox.get())
    par = ''.join([random.choice(chars) for x in range(a)])
    txt=par
    save_ps(txt)
def select():
    result = "Выбрано: "
    if eng.get() == 1: result = f"{result} Английские"
    if ru.get() == 1 and eng.get() == 1: result = f"{result}, Русские"
    if ru.get() == 1 and eng.get() != 1: result = f"{result} Русские"
    if ch.get() == 1 and (ru.get() or eng.get())== 1: result = f"{result}, Цифры и сложные"
    if ch.get() == 1 and ru.get()!=1 and eng.get()!=1: result = f"{result} Цифры и сложные"
    if result!="Выбрано: ": result = f"{result} символы"
    simw.set(result)
 
position = {"padx":6, "pady":6, "anchor":NW}
 
simw = StringVar()
simw_label = ttk.Label(textvariable=simw)
simw_label.pack(**position)
 
eng = IntVar()
eng_checkbutton = ttk.Checkbutton(text="Английские символы", variable=eng, command=select)
eng_checkbutton.pack(**position)
 
ru = IntVar()
ru_checkbutton = ttk.Checkbutton(text="Русские символы", variable=ru, command=select)
ru_checkbutton.pack(**position)
 
ch = IntVar()
ch_checkbutton = ttk.Checkbutton(text="Цифры и символы", variable=ch, command=select)
ch_checkbutton.pack(**position)
selection=0
def selected(event):
    selection = combobox.get()
    print(selection)
    label["text"] = f"Количество символов: {selection}"
 
chisla = ["4", "5", "6", "7", "8", "10", "11", "13", "14", "15", "16", "17", "18", "19", "20"]
label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)
 
combobox = ttk.Combobox(values=chisla, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
btn = ttk.Button(text="Генерация", command=gen)
btn.place(relx=0.5, rely=0.5, anchor="c", width=80, height=40)
root.mainloop()
