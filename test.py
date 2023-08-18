# import math

# # print(math.fabs)

# # print(math.sqrt(16))


# print(math.factorial(10))


# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%d/%m/%y: %H:%M:%S - %a"))


# import time

# def factorial(x):
#     if x <= 1:
#         return 1
#     return x * factorial(x-1)

# start = time.time()
# for i in range(10500):
#     factorial(800)
# stop = time.time()

# total = stop - start

# print(total)


# for i in range(100):
#     time.sleep(10)
#     print(i)


# import random

# names = ["name1", "name2", "name3", "name4"]
# n = random.choice(names)
# print(n)

# import requests

# rq = requests.get("https://www.house.kg/")

# print(rq.text)


# import tkinter as tk

# def button_click():
#     print("Кнопка нажата!")

# # Создаем главное окно
# root = tk.Tk()

# # Устанавливаем заголовок окна
# root.title("Пример приложения")

# # Создаем кнопку
# button = tk.Button(root, text="Нажми меня!", command=button_click)

# # Размещаем кнопку на главном окне
# button.pack()

# # Запускаем главный цикл обработки событий
# root.mainloop()


# import tkinter as tk

# def button_click(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + str(number))

# def button_clear():
#     entry.delete(0, tk.END)

# def button_add():
#     first_number = entry.get()
#     global f_num
#     global math_operation
#     math_operation = "addition"
#     f_num = float(first_number)
#     entry.delete(0, tk.END)

# def button_subtract():
#     first_number = entry.get()
#     global f_num
#     global math_operation
#     math_operation = "subtraction"
#     f_num = float(first_number)
#     entry.delete(0, tk.END)

# def button_multiply():
#     first_number = entry.get()
#     global f_num
#     global math_operation
#     math_operation = "multiplication"
#     f_num = float(first_number)
#     entry.delete(0, tk.END)

# def button_divide():
#     first_number = entry.get()
#     global f_num
#     global math_operation
#     math_operation = "division"
#     f_num = float(first_number)
#     entry.delete(0, tk.END)

# def button_equal():
#     second_number = entry.get()
#     entry.delete(0, tk.END)
#     if math_operation == "addition":
#         entry.insert(tk.END, f_num + float(second_number))
#     elif math_operation == "subtraction":
#         entry.insert(tk.END, f_num - float(second_number))
#     elif math_operation == "multiplication":
#         entry.insert(tk.END, f_num * float(second_number))
#     elif math_operation == "division":
#         entry.insert(tk.END, f_num / float(second_number))

# # Создаем главное окно
# root = tk.Tk()
# root.title("Калькулятор")

# # Создаем поле ввода
# entry = tk.Entry(root, width=40)
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# # Создаем кнопки
# buttons = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["0", ".", "=", "+"]
# ]

# for i, row in enumerate(buttons):
#     for j, button_text in enumerate(row):
#         button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda num=button_text: button_click(num))
#         button.grid(row=i+1, column=j, padx=5, pady=5)

# # Создаем кнопку очистки
# clear_button = tk.Button(root, text="C", padx=20, pady=10, command=button_clear)
# clear_button.grid(row=len(buttons)+1, column=0, padx=5, pady=5, columnspan=2)

# # Создаем кнопки операций
# add_button = tk.Button(root, text="+", padx=20, pady=10, command=button_add)
# add_button.grid(row=1, column=3, padx=5, pady=5)
# subtract_button = tk.Button(root, text="-", padx=20, pady=10, command=button_subtract)
# subtract_button.grid(row=2, column=3, padx=5, pady=5)
# multiply_button = tk.Button(root, text="*", padx=20, pady=10, command=button_multiply)
# multiply_button.grid(row=3, column=3, padx=5, pady=5)
# divide_button = tk.Button(root, text="/", padx=20, pady=10, command=button_divide)
# divide_button.grid(row=4, column=3, padx=5, pady=5)

# # Создаем кнопку равно
# equal_button = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)
# equal_button.grid(row=4, column=2, padx=5, pady=5)

# # Запускаем главный цикл обработки событий
# root.mainloop()