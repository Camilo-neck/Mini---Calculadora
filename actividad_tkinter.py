from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Mi primera aplicacion.')
        self.root.geometry('600x355')
        self.root.iconbitmap("uwu.ico")

        self.Label = tk.Label(self.root, text='Calculadora', font=('Arial Bold', 25))
        self.Label.grid(column=0, row=0)

        self.entrada1 = tk.Entry(self.root, width=20)
        self.entrada2 = tk.Entry(self.root, width=20)

        self.entrada1.grid(column=1, row=1)
        self.entrada2.grid(column=1, row=2)

        self.label_entrada1 = tk.Label(self.root, text='Ingrese el primer numero', font=('Arial Bold', 20))
        self.label_entrada1.grid(column=0, row=1)
        self.label_entrada2 = tk.Label(self.root, text='Ingrese el segundo numero', font=('Arial Bold', 20))
        self.label_entrada2.grid(column=0, row=2)

        self.label_operador = tk.Label(self.root, text='Escoja un operador', font=('Arial Bold', 20))
        self.label_operador.grid(column=0, row=3)
        self.combo_operadores = ttk.Combobox(self.root)
        self.combo_operadores['values'] = ['Escoja una operacion', '+','-','*','/','pow']
        self.combo_operadores.current(0)
        self.combo_operadores.grid(column=1, row=3)

        self.label_resultado = tk.Label(self.root, text='Resultado:', font=('Arial Bold', 40))
        self.label_resultado.grid(column=0, row=6)

        self.label_respuesta = tk.Label(self.root, text='', font=('Arial Bold', 25))
        self.label_respuesta.grid(column=1, row=6)

        self.calcular = tk.Button(self.root, text='Calcular', bg='cyan', fg='black', command=lambda:(self.click_calcular()))
        self.calcular.grid(column=1, row=4)

        self.decimal_var= IntVar()
        self.check_decimales = Checkbutton(self.root, text="¿Desea usar decimales?", font=('Arial Bold', 12),variable = self.decimal_var, onvalue=1, offvalue=0)
        self.check_decimales.grid(column=0, row=5)

        self.varMode = IntVar()
        self.DarkMode = tk.Radiobutton(
            self.root,
            text='Dark',
            variable=self.varMode,
            value=1,
            command=lambda:self.dark_window())
        self.DarkMode.grid(column=2,row=0)
        self.LightMode = tk.Radiobutton(
            self.root,
            text='Light',
            variable=self.varMode,
            value=2,
            command=lambda:self.dark_window())
        self.LightMode.grid(column=3,row=0)

        self.root.mainloop()

    def decimales(self):
        if self.check_decimales==1:
            return True

    def dark_window(self):
        if self.varMode.get() == 1:
            self.root.config(bg="black")
            self.Label.config(bg='black',fg='white')
            self.label_entrada1.config(bg='black',fg='white')
            self.label_entrada2.config(bg='black',fg='white')
            self.label_operador.config(bg='black',fg='white')
            self.label_resultado.config(bg='black',fg='white')
            self.label_respuesta.config(bg='black',fg='white')
            self.calcular.config(bg='red',fg='white')
            self.check_decimales.config(bg='black',fg='white')
            self.DarkMode.config(bg='black',fg='white')
            self.LightMode.config(bg='black',fg='white')
        else:
            self.root.config(bg="white")
            self.Label.config(bg='white',fg='black')
            self.label_entrada1.config(bg='white',fg='black')
            self.label_entrada2.config(bg='white',fg='black')
            self.label_operador.config(bg='white',fg='black')
            self.label_resultado.config(bg='white',fg='black')
            self.check_decimales.config(bg='white',fg='black')
            self.label_respuesta.config(bg='white',fg='black')
            self.calcular.config(bg='cyan', fg='black')
            self.check_decimales.config(bg='white',fg='black')
            self.DarkMode.config(bg='white',fg='black')
            self.LightMode.config(bg='white',fg='black')

    def operaciones(self,num1,num2):
        if self.combo_operadores.get() == '+':
            resultado = num1 + num2
        elif self.combo_operadores.get() == '-':
            resultado = num1 - num2
        elif self.combo_operadores.get() == '*':
            resultado = num1 * num2
        elif self.combo_operadores.get() == '/':
            try:
                resultado = round(num1 / num2,2)
            except ZeroDivisionError:
                messagebox.showerror(
                    "Zero Division Error", "No es posible dividir por 0."
                )
                resultado = ''
        elif self.combo_operadores.get() == 'pow':
            resultado = num1 ** num2
        else:
            messagebox.showwarning(
                "Sin operacion", "Ingrese una operación"
            )
            resultado = ''

        return resultado

    def click_calcular(self):
        try:
            num1 = float(self.entrada1.get())
            num2 = float(self.entrada2.get())
        except ValueError:
            messagebox.showwarning(
                'Empty Values', 'Rellene los campos de valores con valores enteros'
            )
            resultado = ''
            return resultado

        if self.decimal_var.get()==1:
            try:
                res = self.operaciones(num1, num2)
            except ValueError:
                res = ''
        else:
            try:
                res = int(self.operaciones(num1, num2))
            except ValueError:
                res = ''

        self.label_respuesta.configure(text=res)


def main():
    Calculadora()

if __name__ == '__main__':
    main()
