import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from pwd_modules import PWD_string as gen
from pwd_modules import pass_gen as pwd_gen

class Chico_app:
    def generate(self):
        pwd = gen.PWD_string(self.password_length.get())
        chs1 = []
        chs2 = []
        chs3 = []
        chs4 = []
        if self.charset1.get() == 1:
            chs1 = pwd.lettersLOW('all')
        if self.charset2.get() == 1:
            chs2 = pwd.lettersUP('all')
        if self.charset3.get() == 1:
            chs3 = pwd.numbers('all')
        if self.charset4.get() == 1:
            chs4 = pwd.special('all')

        for i in range(self.n_passwd.get()):
            password = pwd_gen.pass_gen(chs1, chs2, chs3, chs4, num=int(pwd)) + "\n"
            self.scr.insert("1.0", password)

        self.scr.clipboard_append(self.scr.get("1.0", tk.END))

    def about(self):
        credits()
        about_text = "PASSWORD GENERATOR:\n\n" \
                     "A program for easily creating secure passwords.\n" \
                     "\nProgrammed by: Josef Němec\n233256 (at) vutbr.cz"
        messagebox.showinfo(title="About", message=about_text)

    def save(self):
        fw = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if fw is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            messagebox.showerror(title="File error", message="The file could not be created!")
            return
        text2save = str(self.scr.get(1.0, tk.END))
        fw.write(text2save)
        fw.close()
        messagebox.showinfo(title="File was created", message="Success!")

    def append(self):
        f_append = filedialog.asksaveasfile(mode='a', defaultextension=".txt")
        if f_append is None:
            messagebox.showerror(title="File error", message="The file could not be opened!")
            return
        text2save = str(self.scr.get(1.0, tk.END))
        f_append.write(text2save)
        f_append.close()
        messagebox.showinfo(title="Data was appended to file", message="Success!")

    def _quit(self):
        self.window.quit()
        self.window.destroy()
        exit()

    def __init__(self, master):
        # Check buttons for Charset box
        self.charset1 = tk.IntVar()
        self.charset2 = tk.IntVar()
        self.charset3 = tk.IntVar()
        self.charset4 = tk.IntVar()
        self.window = master
        self.check_frame = tk.LabelFrame(master, text=' Charset ')
        self.check_frame.grid(column=0, row=0, padx=10, pady=20, sticky="WN")
        tk.Checkbutton(self.check_frame, text="Lower case", variable=self.charset1).grid(column=0, row=0,
                                                                                    padx=10, pady=1, sticky="W")
        tk.Checkbutton(self.check_frame, text="Upper case", variable=self.charset2).grid(column=0, row=1,
                                                                                     padx=10, pady=1, sticky="W")
        tk.Checkbutton(self.check_frame, text="Numbers", variable=self.charset3).grid(column=0, row=2,
                                                                                  padx=10, pady=1, sticky="W")
        tk.Checkbutton(self.check_frame, text="Special characters", variable=self.charset4).grid(column=0, row=3,
                                                                                             padx=10, pady=1,sticky="W")

        # Check buttons for Additional settings box
        self.a = tk.IntVar
        self.b = tk.IntVar
        self.additional_frame = tk.LabelFrame(master, text=' Additional settings ')
        self.additional_frame.grid(column=1, row=0, padx=10, pady=20, sticky="WN")
        self.password_length = tk.StringVar()
        ttk.Label(self.additional_frame, text="Password length: ").grid(column=0, row=0, padx=10, pady=10, sticky="W")
        self.pwd_len = ttk.Combobox(self.additional_frame, width=12, textvariable=self.password_length)
        self.pwd_len.grid(column=1, row=0, padx=10, pady=1, sticky="W")
        self.pwd_len['values'] = (8, 12, 16, 24, 32, 40, 48, 56, 64, 128, 256, 512)
        self.pwd_len.current(1)
        ttk.Label(self.additional_frame, text="Nuber of generated passwords: ").grid(column=0, columnspan=2, row=1,
                                                                                padx=10, pady=6, sticky="W")
        self.n_passwd = tk.Scale(self.additional_frame, from_=1, to=200, orient="horizontal", width=9, length=210)
        self.n_passwd.grid(column=0, columnspan=2, row=2, padx=10, pady=1, sticky="W")

        # ScrolledText configuration
        self.label2 = tk.Label(master, text="Generated Passwords")
        self.label2.grid(column=0, row=3, padx=10, pady=1, sticky="W")
        self.scr = scrolledtext.ScrolledText(master, width=48, height=10, wrap=tk.WORD)
        self.scr.grid(column=0, columnspan=2, row=4, padx=10, pady=1)

        # Buttons configuration
        self.action = ttk.Button(master, text="Generate and copy to clipboard", command=self.generate)
        self.action.grid(column=1, row=5, padx=10, pady=10, sticky="E")
        self.action2 = ttk.Button(master, text="Clear", command=lambda: self.scr.delete(1.0, tk.END))
        self.action2.grid(column=0, row=5, padx=10, pady=10, sticky="W")
        # Menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save As", command=self.save)
        self.file_menu.add_command(label="Append to", command=self.append)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self._quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # About menu
        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label="About", command=self.about)
        self.menu_bar.add_cascade(label="Help", menu=self.about_menu)

        master.title("Chico - Password generator")
        master.resizable(False, False)
