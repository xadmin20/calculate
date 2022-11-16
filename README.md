 
# Калькулятор
## _домашняя работа по лекции №7_

[![Python](http://v1480128.hosted-by-vdsina.ru/img/python.png)](https://www.python.org/)




Калькулятор написан на языке программирования Python версии 3.11. Над дизайном работы не было :)


[![History](http://v1480128.hosted-by-vdsina.ru/img/calc_and_hist.png)]()

`
C:\Users\dobry>python -V
`

`
Python 3.11.0
`

Импортируемые библиотеки (встроенные)

- Tkinter (ver = 8.6)
- log (логирования запросов)
- ✨Magic ✨



## Установка

Скачиваем и устанавливаем ИНТЕРПРЕТА́ТОР [Python3](https://www.python.org/downloads/) v3.8+.

Скачиваем и устанавливаем систему версий [Git](https://git-scm.com/downloads) последней версии.

Запускаем git в терминале:
```sh
git clone git@github.com:xadmin20/calculate.git
```

Или скачиваем по ссылке

https://github.com/xadmin20/calculate.git


## Запуск

### Windows:
`
Win+R --> cmd --> python <dir>/main.py
`
### Ubuntu:
`
Ctrl+Alt+T --> puthon3 <dir>/main.py
`
## Лицензия

- Свободное использование, без ограничений.

**Free Software, Hell Yeah!**

## Code:

* Импортируем необходимые библиотеки:
```
from tkinter import *
import log
```

* Создаем окно с названием калькулятор:
```python
root = Tk()
root.geometry("315x370")
# root.resizable(0, 0)
root.title("Калькулятор")
```

* Создаем поле показа вводы цифр и вывода результата:
```python
input_text = StringVar()
input_frame = Frame(root, width = 250, height = 50, bd = 0, highlightbackground = "black",
                    highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text,
                    width = 50, bg = "#eee", bd = 0, justify = RIGHT)
```

* Создаем кнопки:
```python
btns_frame = Frame(root, width = 469, height = 372.5, bg = "#000")
btns_frame.pack()
git = Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#0DE3DB", cursor = "hand2",
               command = lambda: btn_click("(")).grid(row = 0, column = 1, columnspan = 1, padx = 1, pady = 1)
git2 = Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#0DE3DB", cursor = "hand2",
               command = lambda: btn_click(")")).grid(row = 0, column = 2, columnspan = 1, padx = 1, pady = 1)
clear = Button(btns_frame, text = "Clear", fg = "black", width = 10, height = 3, bd = 0, bg = "#f00", cursor = "hand2",
               command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#0DE3DB", cursor = "hand2",
                command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
seven = Button(btns_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "#2B6B06", cursor = "hand2",
               command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "#2B6B06", cursor = "hand2",
               command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "#2B6B06", cursor = "hand2",
              command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#0DE3DB", cursor = "hand2",
                  command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
four = Button(btns_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#2B6B06", cursor = "hand2",
              command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#2B6B06", cursor = "hand2",
              command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#2B6B06", cursor = "hand2",
             command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1
```

