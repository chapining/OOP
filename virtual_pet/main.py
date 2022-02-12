import tkinter as tk
from pet import Pet


class App(tk.Tk):
    """docstring for App"""
    def __init__(self):
        super().__init__()
        self.pet = Pet(
            name="Бобрик",
            portrait="asserts/calm.png"
        )

        self.canvas = tk.Canvas(self, width=300, height=200)
        self.canvas.pack()
        self.image = tk.PhotoImage(file=self.pet.portrait)
        self.canvas.create_image(0, 0, image=self.image)
        """
            TODO: 
                кнопочки:
                    корм
                    питьё
                    играть
                    спать
                лейблы:
                    атрибуты питомца
                портре:
                    как изменяется картинка портрета
                    мб mood?
                    мб состояния?

        """

window = App()
window.mainloop()
