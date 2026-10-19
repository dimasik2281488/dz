import tkinter as tk

first = None      
operator = None   
typed = ""        
fresh = False     


def show():
    """Обновляет поле вывода (text_input)."""
    left = "" if first is None else f"{fmt(first)} {operator or ''} "
    text_input.config(text=left + typed)


def fmt(x):
    return str(int(x)) if float(x).is_integer() else str(round(x, 8))



def press_number(n):
    global typed, first, operator, fresh
    if fresh:                     
        first, operator, typed, fresh = None, None, "", False
    typed += str(n)
    show()



def choose_operator(sign):
    """Запоминает первое число и знак операции."""
    global first, operator, typed, fresh
    if typed == "" and first is None:
        return
    if typed != "" and first is not None and operator:
        result()                  
    if typed != "":
        first = float(typed)
    typed, operator, fresh = "", sign, False
    show()


def multiply():
    choose_operator("*")


def divide():
    choose_operator("%")         


def summy():
    choose_operator("+")


def diff():
    choose_operator("-")


def result():
    global first, operator, typed, fresh
    if first is None or operator is None or typed == "":
        return
    b = float(typed)
    if operator == "*":
        r = first * b
    elif operator == "%":
        if b == 0:
            text_input.config(text="Деление на 0")
            first, operator, typed, fresh = None, None, "", True
            return
        r = first / b
    elif operator == "+":
        r = first + b
    else:
        r = first - b
    first, operator, typed, fresh = None, None, fmt(r), True
    show()



root = tk.Tk()
root.title("Калькулятор")
root.resizable(False, False)


text_input = tk.Label(root, text="", anchor="e", bg="white", relief="sunken",
                      font=("Arial", 18), width=18, padx=6, pady=6)
text_input.grid(row=0, column=0, columnspan=4, padx=6, pady=6, sticky="we")


for n in range(10):
    btn = tk.Button(root, text=str(n), width=5, height=2, font=("Arial", 14),
                    command=lambda d=n: press_number(d))
    if n == 0:
        btn.grid(row=4, column=0, columnspan=2, sticky="we", padx=2, pady=2)
    else:
        btn.grid(row=(9 - n) // 3 + 1, column=(n - 1) % 3, padx=2, pady=2)


operations = [
    ["multiply", "*"],
    ["divide",   "%"],
    ["summy",    "+"],
    ["diff",     "-"],
    ["result",   "="],
]


for i in range(len(operations)):
    func_name, sign = operations[i]
    tk.Button(root, text=sign, width=5, height=2, font=("Arial", 14),
              command=globals()[func_name]      
              ).grid(row=i + 1, column=3, padx=2, pady=2)

root.mainloop()
