import tkinter as tk

root = tk.Tk()

root.title("Приветствие")

label = tk.Label(root, text = "Введите Ваше имя")

label.grid(row=1)

entry = tk.Entry(root, justify = "center")
entry.grid(row=0)

def button_click():
    name = entry.get()
    label.config (text=f"Привет, {name}!")

button = tk.Button(root, text="Поздороваться", command=button_click)

button.grid(row=2)

root.mainloop()
