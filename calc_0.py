import tkinter as tk
from tkinter import messagebox as mb

class App(tk.Tk):
    def calculate_currency(self):
        user_money = self.money_ent.get()
        try:
            int(user_money)
        except ValueError:
            mb.showwarning("ошибка данных", "Сумма не интуется")
        else:
            result = round(int(user_money) * self.rate_user.get() / self.rate_result.get(), 2)
            self.my_lbl.config(text=result)


    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("800x600")
        self.my_lbl = tk.Label(
            self,
            text="результат в доллорах"
        )
        
        self.my_btn = tk.Button(
            self,
            text = "рассчёт",
            command=lambda: self.calculate_currency()
        )
        
        self.money_ent = tk.Entry(self)
        self.rate_result = tk.DoubleVar()
        self.rate_result.set(74.67)
        self.rate_user = tk.DoubleVar()
        self.rate_user.set(1)
        self.cur_0 = tk.Radiobutton(
            self,
            text="доллар США",
            variable=self.rate_result,
            value=74.67
        )
        self.cur_1 = tk.Radiobutton(
            self,
            text="Кувейтский динар",
            variable=self.rate_result,
            value=246.91
        )
        self.cur_2 = tk.Radiobutton(
            self,
            text="Иранский риал",
            variable=self.rate_result,
            value=0.0018
        )
        self.cur_3 = tk.Radiobutton(
            self,
            text="Российский рубль",
            variable=self.rate_result,
            value=1
        )
        self.usr_0 = tk.Radiobutton(
            self,
            text="доллар США",
            variable=self.rate_user,
            value=74.67
        )
        self.usr_1 = tk.Radiobutton(
            self,
            text="Кувейтский динар",
            variable=self.rate_user,
            value=246.91
        )
        self.usr_2 = tk.Radiobutton(
            self,
             text="Иранский риал",
            variable=self.rate_user,
            value=0.0018
        )
        self.usr_3 = tk.Radiobutton(
            self,
            text="Российский рубль",
            variable=self.rate_user,
            value=1
        )

        self.my_lbl.pack()
        self.money_ent.pack()
        self.cur_0.pack()
        self.cur_1.pack()
        self.cur_2.pack()
        self.cur_3.pack()
        
        self.usr_0.pack()
        self.usr_1.pack()
        self.usr_2.pack()
        self.usr_3.pack()
        self.my_btn.pack()

        
window = App("Окно")
window.mainloop()