# -*- coding: utf-8 -*-
"""
Proyecto de Primer Parcial
Luis Javier Origel Gonzalez
Gonzalo Magallanes
"""
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
    #%% Pagina Principal
def main():
    windowsmaster = Tk()
    windowsmaster.title("Vectoriños")
    windowsmaster.geometry("400x300")
    windowsmaster.configure( bg= "#2D572C")
    
    #%%Funciones No GUI
    def delete(window):
        window.destroy()
    
    #%% Titulo
    lbltest = Label(windowsmaster,text = "ᐯ乇匚ㄒㄖ尺丨几ㄖ丂")
    lbltest.place(x=3,y=10)
    lbltest.configure(bg = "brown",fg = "white", font=('Arial',30))
    
    #%% Suma y Resta de Vcetores
    def sumar_restar():
        delete(windowsmaster)
        windowsum = Tk()
        windowsum.title("Suma y Resta de Vectores")
        windowsum.geometry("600x400")
        windowsum.configure( bg= "#2D572C")
        
        #Titulo
        lbltitulosr = Label(windowsum, text = "丂ㄩ爪卂 ㄚ 尺乇丂ㄒ卂")
        lbltitulosr.configure(bg = "black",fg = "white", font=('Arial',30))
        lbltitulosr.place( x= 85, y= 10)
        
        # X
        lblsumx = Label(windowsum, text = "Inserte X")
        lblsumx.place(x=45,y =90)
        lblsumx.configure(bg = "black",fg = "white", font=('Nordic',12))
        
        txtsumx = Entry(windowsum)
        txtsumx.configure(bg = "green")
        txtsumx.place(x=20,y=110)
        
        # Y
        lblsumy = Label(windowsum,  text = "Inserte Y")
        lblsumy.place(x=45,y =170)
        lblsumy.configure(bg = "black",fg = "white", font=('Nordic',12))
        
        txtsumy = Entry(windowsum)
        txtsumy.configure(bg = "green")
        txtsumy.place(x=20,y=190)
        
        # Respuesta
        lblnumero = Label(windowsum, text = "")
        lblnumero.place(x= 400, y=90)
        lblnumero.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        
        lblnumeroans =  Label(windowsum, text = "")
        lblnumeroans.place(x= 410, y=110)
        lblnumeroans.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        
        # Suma
        def sumar():
            X , Y = str(txtsumx.get()), str(txtsumy.get())
            listX , listY = list(map(int,X.split(","))), list(map(int,Y.split(",")))
            sumx , sumy = sum(listX) , sum(listY)
            texto = "{},{}".format(sumx,sumy)
            lblnumero.configure(text="Numero ")
            lblnumeroans.configure(text= texto)
            
        btnsuma = Button(windowsum, text="Sumar", command = sumar)
        btnsuma.place(x=45, y=300)
        btnsuma.configure(bg = "brown",fg = "white", font=('Nordic',12))
        
        # Restar
        def restar():
            X , Y = str(txtsumx.get()), str(txtsumy.get())
            listX , listY = list(map(int,X.split(","))), list(map(int,Y.split(",")))
            totalx , totaly = 2 * listX[0], 2 * listY[0]
            [totalx := totalx - x for x in listX]
            [totaly := totaly - x for x in listY]
            texto = "{},{}".format(totalx,totaly)
            lblnumero.configure(text="Numero ")
            lblnumeroans.configure(text= texto)
            
        btnrestar = Button(windowsum, text="Restar", command = restar)
        btnrestar.place(x=250, y=300)
        btnrestar.configure(bg = "brown",fg = "white", font=('Nordic',12))
        
        #Salir
        def regresarsum():
            windowsum.destroy()
            main()
        btnsalirsum = Button(windowsum, text="Salir", command = regresarsum)
        btnsalirsum.place(x=480, y=300)
        btnsalirsum.configure(bg = "brown",fg = "white", font=('Nordic',12), width = 6)
        
        #ver_mas
        def ver_mas():
            windowsum.geometry("600x600")
        lbl1_linea = Label(windowsum, text ="La suma de vectores se logra sumando las 'x' y las 'y'")
        lbl2_linea = Label(windowsum, text ="por separado, asi generando la suma de vectores")
        lbl3_linea = Label(windowsum, text ="(sum de x, sum de y)")
        lbl1_linea.place(x=10,y= 460)
        lbl1_linea.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        lbl2_linea.place(x=10,y= 480)
        lbl2_linea.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        lbl3_linea.place(x=10,y= 500)
        lbl3_linea.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        btn_ver_mas = Button(windowsum, text = "ver mas...", command = ver_mas)
        btn_ver_mas.place(x= 480, y=350)
        btn_ver_mas.configure(bg = "brown",fg = "white", font=('Nordic',8), width = 10)
        
        #ver_menos
        def ver_menos():
            windowsum.geometry("600x400")
        
        btn_ver_menos = Button(windowsum, text="Ver menos...", command = ver_menos)
        btn_ver_menos.place(x= 480, y=480)
        btn_ver_menos.configure(bg = "brown",fg = "white", font=('Nordic',8), width = 10)
        windowsum.mainloop()
    
    lblsuma_resta = Label(windowsmaster, text = "Suma y Resta de vectores")
    lblsuma_resta.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
    lblsuma_resta.place(x= 40, y=100)
    
    btnsuma_resta = Button(windowsmaster,text = "Calcular", command = sumar_restar)
    btnsuma_resta.place(x=280, y=100)
    btnsuma_resta.configure(bg = "brown", width = 10,fg = "white")
    
    #%% Magnitud y Angulo de vectores
    def magnitud():
        delete(windowsmaster)
        windowmag = Tk()
        windowmag.title("Magnitud y Angulo de vectores")
        windowmag.geometry("600x200")
        windowmag.configure(bg= "#2D572C")
        #Titulo
        lbltitulo = Label(windowmag, text = "ᗰᗩGᑎITᑌᗪ Y ᗩᑎGᑌᒪO ᗪE ᐯEᑕTOᖇEᔕ")
        lbltitulo.place(x=0,y=0)
        lbltitulo.configure(bg = "red",fg = "black", font=('Arial',24))
        #Sacar Magnitud
        lblmag = Label(windowmag, text="Inserte la X y Y y se sacara su magnitud")
        lblmag.place(x=15,y=50)
        lblmag.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        txtmag = Entry(windowmag)
        txtmag.place(x=15,y=70)
        lblinfomag = Label(windowmag, text="")
        lblinfomag.place(x=350,y=50)
        lblinfomag.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        
        
        lblinfoang = Label(windowmag, text="")
        lblinfoang.place(x=350,y=120)
        lblinfoang.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        
        
        lblansmag = Label(windowmag,text="")
        lblansmag.place(x=350,y=70)
        lblansmag.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        
        
        lblansang = Label(windowmag,text="")
        lblansang.place(x=350,y=140)
        lblansang.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        
        #Calcular Angulo y Magnitud
        def Calcular():
            value = txtmag.get()
            [listmag := list(value.split(","))]
            x,y = int(listmag[0]),int(listmag[1])
            txtmag.delete(0,END)
            array = np.array([x,y])
            magnitud = np.linalg.norm(array)
            angulo = np.arctan(array[1]/array[0])*180/np.pi
            if angulo<0:
                angulo = 180-angulo
                
            lblinfoang.configure(text= "Angulo")
            lblinfomag.configure(text="Magnitud")
            lblansmag.configure(text = magnitud)
            lblansang.configure(text = angulo)
        
        btncalcular = Button(windowmag, text="Calcular", command= Calcular)
        btncalcular.place(x=15,y=150)
        btncalcular.configure(bg = "brown", width = 10,fg = "white")
        
        #Explicacion
        lbltext_1 = Label(windowmag, text="La magnitud es la forma en la que se miden las dimensiones de una linea")
        lbltext_2 = Label(windowmag, text="y estas se miden en unidades")
        lbltext_3 = Label(windowmag, text="El angulo de una recta es la inclinacion con la cual se mide una recta")
        lbltext_4 = Label(windowmag, text="y este se mide en grados°")
        
        lblformulamag = Label(windowmag, text="v = √(x2 + y2))")
        lblformulaang = Label(windowmag, text="arctan(y/x) * 180 / π")
        
        lbltext_1.place(x=15, y=260)
        lbltext_2.place(x=15, y=280)
        lbltext_3.place(x=15, y=300)
        lbltext_4.place(x=15, y=320)
        
        lblformulamag.place(x=430,y=280)
        lblformulaang.place(x=430,y=320)
        
        lbltext_1.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        lbltext_2.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        lbltext_3.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        lbltext_4.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
        
        lblformulamag.configure(bg = "#2D572C",fg = "red", font=('Nordic',12))
        lblformulaang.configure(bg = "#2D572C",fg = "red", font=('Nordic',12))
        
        #ver mas
        def ver_mas():
            windowmag.geometry("600x400")
            
        btn_ver_mas = Button(windowmag, text="Ver mas...", command= ver_mas)
        btn_ver_mas.place(x=100, y=150)
        btn_ver_mas.configure(bg = "brown", width = 10,fg = "white")
        
        #Ver menos
        def ver_menos():
            windowmag.geometry("600x200")
        
        btn_ver_menos = Button(windowmag, text="Ver menos", command= ver_menos)
        btn_ver_menos.place(x=430,y=360)
        btn_ver_menos.configure(bg = "brown", width = 10,fg = "white")
        
        def regresarmag():
            windowmag.destroy()
            main()
        
        btn_salir = Button(windowmag, text="Salir", command=regresarmag)
        btn_salir.place(x=185,y=150)
        btn_salir.configure(bg = "brown", width = 10,fg = "white")
        windowmag.mainloop()
    
    lblmagnitud = Label(windowsmaster,text = "Magnitud y Angulo de vectores")
    lblmagnitud.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
    lblmagnitud.place(x= 40, y=170)
    
    btn_magnitud = Button(windowsmaster,text = "Calcular", command = magnitud)
    btn_magnitud.place(x=280, y=170)
    btn_magnitud.configure(bg = "brown", width = 10,fg = "white")
    
    
    #%% Graficar Vectores
    def graficar():
        delete(windowsmaster)
        windowgra = Tk()
        windowgra.title("Graficar Vectores")
        windowgra.geometry("600x400")
        windowgra.configure(bg= "#2D572C")
        
        lbltitulograf = Label(winodwgra, text="Graficar Vectores")
        
        windowgra.mainloop()
    
    lblgraficar = Label(windowsmaster,text = "Graficar Vectores")
    lblgraficar.configure(bg = "#2D572C",fg = "white", font=('Nordic',12))
    lblgraficar.place(x= 40, y=240)
    
    btn_graficar = Button(windowsmaster,text = "Graficar", command = graficar)
    btn_graficar.place(x=280, y=240)
    btn_graficar.configure(bg = "brown", width = 10,fg = "white")
    
    windowsmaster.mainloop()


    #%% Ejecucion
if __name__ == "__main__":
    main()
    