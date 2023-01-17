import tkinter as tk
import customtkinter as ctk

from functions import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

        self.title("Phase 10 Probability")
        self.minsize(400, 300)

        self.button = ctk.CTkButton(master="ah", command=generateHands(100))
        self.button.pack(padx=20, pady=20)




if __name__ == "__main__":
    app = App()
    app.mainloop()