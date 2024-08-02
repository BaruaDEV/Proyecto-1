from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadro_comida:
        if variables_comida[x].get() ==1:
            cuadro_comida[x].config(state=NORMAL)
            if cuadro_comida[x].get() == '0':
                cuadro_comida[x].delete(0,END)
            cuadro_comida[x].focus()
        else:
            cuadro_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadro_bebida:
        if variables_bebida[x].get() ==1:
            cuadro_bebida[x].config(state=NORMAL)
            if cuadro_bebida[x].get() == '0':
                cuadro_bebida[x].delete(0,END)
            cuadro_bebida[x].focus()
        else:
            cuadro_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadro_postre:
        if variables_postre[x].get() ==1:
            cuadro_postre[x].config(state=NORMAL)
            if cuadro_postre[x].get() == '0':
                cuadro_postre[x].delete(0,END)
            cuadro_postre[x].focus()
        else:
            cuadro_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1    


def total():
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get()) * precios_postre[p])
        p += 1    

    sub_total = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = sub_total * 0.07  ## este 0.07 es si el impuesto al valor agregado es de 7% (a modo de ejemplo)
    total = sub_total + impuestos

    var_costo_comidas.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebidas.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postres.set(f'$ {round(subtotal_postre, 2)}')

    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 65 + '\n' )
    texto_recibo.insert(END, 'Items\t\tCant.\t\tCosto Items\n' )
    texto_recibo.insert(END, f'-' * 80 +'\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t\t'
                                f'$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x=0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t\t'
                                f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x=0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t\t'
                                f'$ {int(postre.get()) * precios_postre[x]}\n')
        x += 1       

    texto_recibo.insert(END, f'*' * 65 + '\n' )
    texto_recibo.insert(END, f'Costo de la comida: \t\t\t\t {var_costo_comidas.get()}\n')
    texto_recibo.insert(END, f'Costo de la bebidas: \t\t\t\t {var_costo_bebidas.get()}\n')
    texto_recibo.insert(END, f'Costo de la postres: \t\t\t\t {var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'*' * 65 + '\n' )
    texto_recibo.insert(END, f'Subtotal: \t\t\t\t {var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t\t {var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t\t {var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 65 + '\n' )
    texto_recibo.insert(END, f'\t**** Lo esperamos pronto ****')

def guardar():  
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información','su recibo ah sido guardado')

def resetear():
    texto_recibo.delete(0.1,END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comidas.set('')
    var_costo_bebidas.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')

# Iniciar TKinder
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1080x630+0+0')

#EVitar maximizar
aplicacion.resizable(False,False)

# Titulo del programa ventana
aplicacion.title("Mi restaurante - Sistema de Facturacion")

# Color del fondo de la ventana
aplicacion.config(bg='burlywood')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturación' , fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=20)
etiqueta_titulo.grid(row=0, column=0)

#Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel Costos izquierdo inferior
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=60)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_camidas = LabelFrame(panel_izquierdo, text='Comidas', font=('Dosis',19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_camidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='bebidas', font=('Dosis',19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis',19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# PANEL DERECHA
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel_calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#panel_recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#panel_botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista de productos

lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza' , 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola' , 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse' , 'pastel1' , 'pastel2', 'pastel3']


# Generear items de comidas
variables_comida=[]
cuadro_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:

    ## crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_camidas,
                         text=comida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row= contador, column=0, sticky=W)

    ## crear cuadros de comida
    cuadro_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadro_comida[contador] = Entry(panel_camidas,
                                    font=('Dosis',18,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador])
    cuadro_comida[contador].grid(row=contador, column=1)
    contador +=1


# Generear items de bebidas
variables_bebida=[]
cuadro_bebida = []
texto_bebida = []
contador = 0

for bebida in lista_bebidas:

    ## crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row= contador, column=0, sticky=W)

    ## crear cuadros bebidas
    cuadro_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadro_bebida[contador] = Entry(panel_bebidas,
                                    font=('Dosis',18,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador])
    cuadro_bebida[contador].grid(row=contador, column=1)  

    contador +=1

# Generear items de postres
variables_postre=[]
cuadro_postre = []
texto_postre = []
contador = 0

for postre in lista_postres:

    ## crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    
    postre.grid(  row  = contador,
                column = 0,
                sticky = W)

    ## crear los cuadros de entrada
    cuadro_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadro_postre[contador] = Entry(panel_postres,
                                    font=('Dosis',18,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postre[contador])
    cuadro_postre[contador].grid(row=contador, column=1)
    contador +=1

## variables
var_costo_comidas = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_impuestos = StringVar()
var_subtotal = StringVar()
var_total= StringVar()


## etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='costo comidas',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                              font=('Dosis',12, 'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_costo_comidas)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text='costo bebidas',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                              font=('Dosis',12, 'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_costo_bebidas)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(panel_costos,
                              text='costo postres',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                              font=('Dosis',12, 'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_costo_postres)
texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                              font=('Dosis',12, 'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                              font=('Dosis',12, 'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                              font=('Dosis',12, 'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

## BOTONES DE LA CONSOLA
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',13,'bold'),
                   fg="white",
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

## area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=45,
                    height=10)
texto_recibo.grid(row=0, column=0)

## CALCULADORA
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=35,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','Resultado','Borrar','0','/']
botones_guardados = []
fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',14,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1
    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

# evitar que la pantalla se cierre (Siempre al final del codigo)
aplicacion.mainloop()