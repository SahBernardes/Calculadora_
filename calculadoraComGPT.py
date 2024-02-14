'''Pedi ao GPT para criar um codigo de uma calculadora porem esse codigo deveria ter erros
para que eu possa praticar a verificação e correção de codigos que não foram feitos por mim'''
import tkinter as tk

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")

        self.entry = tk.Entry(master, width=16, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, width=4, height=2, font=('Arial', 16),
                               command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column)

    def button_click(self, value):
        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
