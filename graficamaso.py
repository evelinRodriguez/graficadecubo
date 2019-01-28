from tkinter import*

raiz=Tk()

raiz.title("ventana de prueba")
raiz.config(bg="blue")
#cambiar el color de la ventana
raiz.resizable(1,0)
#eso significa que nos e puede redimencionar el cuadro en 0,0
raiz.geometry("650x650")
#acmbiar el tamaño de la ventana
raiz.iconbitmap("45854673_286023295356968_8089437027885383680_n.ico")
#para cambiar la imagen de la ventana toca convertirla en .ico yluego ponerla en el mismo directorio
myFrame=Frame()
myFrame.pack(side="bottom",anchor="w")#bottom para abajo, tambie sirve con los putos cardinales, fill=x se queda una linea del color en cuestiono , obvio sin las otras dos propiedades, para redimencionar en y es fill="y",expand="true"
#un frame empaquetado en la raiz
myFrame.config(bg="pink")
myFrame.config(width="350", height="350")
#para bordes
myFrame.config(bd=35)
#hay muchos bordes
myFrame.config(relief="groove")
myFrame.config(cursor="pirate")

raiz.mainloop()
#bucleinfinito para que la ventana este abierta
#buscar tkinter options en wiki
#agregar w depues del .py para q se ejecute el programa sin la consola detras
