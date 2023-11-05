from customtkinter import *
from random import randint

# Главное окно
root = CTk()

# Заголовок программы
root.title('Рандомайзер до 100')

# Фрейм
frame = CTkFrame(master=root, width=300, height=350, corner_radius=17, border_width=3, border_color='#DC6457')
frame.pack(pady=20, padx=20)

# Окно вывода числа
label = CTkLabel(master=frame, width=190, height=20, text='Нажми на кнопку', 
                 text_color='#9900FF', font=('ALS Hauss', 30), fg_color='#EFECFE', corner_radius=10)
label.place(relx=0.5, rely=0.2, anchor='center')

# Работа слайдера
def range_selection(value):
    num.set(f'{int(slider.get())}')

# Слайдер
slider = CTkSlider(master=frame, from_=0, to=100, border_width=3, 
                   progress_color=("#252525","#7FAAFB"), button_color="#0997F1", command=range_selection)
slider.place(relx=0.5, rely=0.4, anchor='center')
num = StringVar(value="")

# Текст
text_frame = CTkLabel(master=frame, width=100, height=1, text='Диапазон от 0 до ', font=('HeliosExtC', 20), text_color="#EFECFE")
text_frame.place(relx=0.07, rely=0.54)

# Окно ввода диапазона
check_num = CTkEntry(master=frame, width=56.5, height=25, textvariable=num,
                     corner_radius=8, fg_color='#252525', text_color='#CAD170', font=('HeliosExtC', 20), border_color="#DC6457")
check_num.place(relx=0.75, rely=0.529)

# Функция нажатия на кнопку
def generate(event):
    label.configure(text=randint(0, int(slider.get())))
    slider.set(int(check_num.get()))

# Кнопка генерации
btn = CTkButton(master=frame, width=100, height=35, 
                text='Выбрать число', corner_radius=11, font=('Jost', 20), fg_color='#D3B69E', text_color='#192F35')
btn.place(relx=0.5, rely=0.8, anchor='center')

# Захват нажатия
btn.bind('<Button-1>', command=generate)


def quit(event):
    root.quit()

# Кнопка выхода
btn_quit = CTkButton(master=frame, width=70, height=25, 
                text='Выход', corner_radius=11, font=('Jost', 20), fg_color='#EFECFE', text_color='#252525')
btn_quit.place(relx=0.5, rely=0.92, anchor='center')

# Захват нажатия
btn_quit.bind('<Button-1>', command=quit)

# Запуск программы
root.mainloop()