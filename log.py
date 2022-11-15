#файл логирования
import datetime
import socket
from tkinter import *


file = "logger.txt"


def log_add(message):
    t = datetime.datetime.now()
    with open(file, "a+", encoding="UTF-8") as f:
        f.write(f"\n{t}|{socket.gethostname()}|{message}")
    print(f"{t}:{message}")


def log_list():
    result = ''
    with open(file, "r", encoding="UTF-8") as f:
        res = f.readlines()
    for i in res:
        i = i.strip()
        date = i.split('|')[0]
        result = result + f"Дата: [{date.split('.')[0]}] | Имя: [{i.split('|')[1]}] | Действие: [{i.split('|')[2]}] \n"
    window = Tk()
    window.title("История запросов: ")
    lbl = Label(window, text=result)
    lbl.grid(column=0, row=0)
    window.mainloop()
