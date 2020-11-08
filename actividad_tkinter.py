from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def init_window():
    root = tk.Tk()
    root.title('Mi primera aplicacion.')
    root.geometry('600x355')
    root.iconbitmap("uwu.ico")

    Label = tk.Label(root, text='Calculadora', font=('Arial Bold', 25))
    Label.grid(column=0, row=0)

    entrada1 = tk.Entry(root, width=20)
    entrada2 = tk.Entry(root, width=20)

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    label_entrada1 = tk.Label(root, text='Ingrese el primer numero', font=('Arial Bold', 20))
    label_entrada1.grid(column=0, row=1)
    label_entrada2 = tk.Label(root, text='Ingrese el segundo numero', font=('Arial Bold', 20))
    label_entrada2.grid(column=0, row=2)

    label_operador = tk.Label(root, text='Escoja un operador', font=('Arial Bold', 20))
    label_operador.grid(column=0, row=3)
    combo_operadores = ttk.Combobox(root)
    combo_operadores['values'] = ['Escoja una operacion', '+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(root, text='Resultado:', font=('Arial Bold', 40))
    label_resultado.grid(column=0, row=6)

    label_respuesta = tk.Label(root, text='', font=('Arial Bold', 25))
    label_respuesta.grid(column=1, row=6)

    calcular = tk.Button(root, text='Calcular', bg='cyan', fg='black', command=lambda:(click_calcular(label_respuesta, entrada1.get(), entrada2.get(), combo_operadores.get(),decimales(decimal_var))))
    calcular.grid(column=1, row=4)

    decimal_var= IntVar()
    check_decimales = Checkbutton(root, text="¿Desea usar decimales?", font=('Arial Bold', 12),variable = decimal_var, onvalue=1, offvalue=0)
    check_decimales.grid(column=0, row=5)

    varMode = IntVar()
    DarkMode = tk.Radiobutton(
        root,
        text='Dark',
        variable=varMode,
        value=1,
        command=lambda:dark_window(
            root,Label,label_entrada1,label_entrada2,label_operador,label_resultado,label_respuesta,calcular,check_decimales,varMode
        ))
    DarkMode.grid(column=2,row=0)
    LightMode = tk.Radiobutton(
        root,
        text='Dark',
        variable=varMode,
        value=2,
        command=lambda:dark_window(
            root,Label,label_entrada1,label_entrada2,label_operador,label_resultado,label_respuesta,calcular,check_decimales,varMode
        ))
    LightMode.grid(column=3,row=0)

    root.mainloop()

def decimales(check_var):
    if check_var.get()==1:
        return True

def dark_window(window,title,label1,label2,operador,resultado,respuesta, calcular,decimales,varMode):
    if varMode.get() == 1:
        window.config(bg="black")
        title.config(bg='black',fg='white')
        label1.config(bg='black',fg='white')
        label2.config(bg='black',fg='white')
        operador.config(bg='black',fg='white')
        resultado.config(bg='black',fg='white')
        respuesta.config(bg='black',fg='white')
        calcular.config(bg='red',fg='white')
    else:
        window.config(bg="white")
        title.config(bg='white',fg='black')
        label1.config(bg='white',fg='black')
        label2.config(bg='white',fg='black')
        operador.config(bg='white',fg='black')
        resultado.config(bg='white',fg='black')
        decimales.config(bg='white',fg='black')
        respuesta.config(bg='white',fg='black')
        calcular.config(bg='cyan', fg='black')

def operaciones(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        try:
            resultado = round(num1 / num2,2)
        except ZeroDivisionError:
            messagebox.showerror(
                "Zero Division Error", "No es posible dividir por 0."
            )
            resultado = ''
    elif operador == 'pow':
        resultado = num1 ** num2
    else:
        resultado = 'Esocoja una operación'

    return resultado

def click_calcular(label, num1, num2, operador, check_fun=False):
    try:
        valor1 = float(num1)
        valor2 = float(num2)
    except ValueError:
        messagebox.showwarning(
            'Empty Values', 'Rellene los campos de valores'
        )
        resultado = ''
        return resultado

    if check_fun==True:
        try:
            res = operaciones(valor1, valor2, operador)
        except ValueError:
            res = ''
    else:
        try:
            res = int(operaciones(valor1, valor2, operador))
        except ValueError:
            res = ''

    label.config(text=res)


def main():
    init_window()

if __name__ == '__main__':
    main()
