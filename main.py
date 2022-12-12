import tkinter as tk
from pwd_modules import gui


if __name__ == "__main__":
    win = tk.Tk()
    app = gui.Chico_app(win)
    app.about()
    win.mainloop()
