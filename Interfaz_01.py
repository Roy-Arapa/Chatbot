#-------------------------------------------------LIBRERIAS PARA EL INTERFAZ-------------------------------
from tkinter import *                            #------ Importando todas la librerias de tkinter
from tkinter import ttk                          #------ Alias de ttk
import tkinter as tk                             #------ Alias de tk  
from PIL import Image, ImageTk                   #------ Modificar imagen (Tamaño)
from datetime import date, datetime              #------ Fecha
from Hablar import Obtener_respuesta, Nombre_Bot #------ Envia Valores Hablar.py
from tkinter import filedialog                   #------ Abre cualquier archivo 
#----------------------------------------------------------------------------------------------------------
#------------------------------------------------LIBRERIAS PARA EL AUDIO-----------------------------------
import speech_recognition as sr                 #------ Convertir de voz a texto.
from gtts import gTTS                           #------ Convertir de teto a voz.
from playsound import playsound                 #------ Reproducir voz.
from os import remove                           #------ Eliminar.
import shutil                                   #------ Copiar archivo.
import os.path                                  #------ verificar el nombre de una carpeta.
#---------------------------------------------------------------------------------------------------------


#-------------------------------------------
#            FUNCIONES
#-------------------------------------------

class Pestaña1(ttk.Frame):
    
    """Pestaña 1, Agregar Nombre"""
    
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        
        #-------Funciones
        self.Crear_Widgets()
        self.Cuadro()
    
    def Cuadro(self):
        self.canvas = Canvas(self, height=350, width=470)
        self.canvas.grid(column=0, row=0, sticky='NW', padx=0, pady=20)
        self.canvas.create_rectangle(20, 10, 450, 340, fill="white", outline="gainsboro") 
        
    def Crear_Widgets(self):
        
        #----------text variables
        self.DNI = tk.StringVar()
        self.Nombre = tk.StringVar()    
        self.Apellidos = tk.StringVar()
        self.Edad = tk.StringVar()
        
        #----------Buttons
        self.button1 = ttk.Button(self, text="Agregar", cursor="hand2").grid(row=1, column=0, sticky='NW', padx=200, pady=130) 

       
        #----------Label
        self.label1 = ttk.Label(self, text="Nombre:").grid(row=1, column=0, sticky='NW', padx=20, pady=10)
        self.label2 = ttk.Label(self, text="Genero:").grid(row=1, column=0, sticky='NW', padx=20, pady=40)

        #----------Text boxes
        self.textbox3 = ttk.Entry(self, textvariable=self.Nombre).grid(row=1, column=0, sticky='NW', padx=100, pady=10)
        
        #---------Radiobutton
        self.radioButton1 = ttk.Radiobutton(self, text="Masculino", value=1).grid(row=1, column=0, sticky='NW', padx=100, pady=40)
        self.radioButton1 = ttk.Radiobutton(self, text="Femenino", value=1).grid(row=1, column=0, sticky='NW', padx=190, pady=40)
    
#---------------------------------------------------------------------------------------------------------------------------------------------        
        
class Pestaña2(ttk.Frame):
    
    """Pestaña 2, Chatbot"""
    
    def __init__(self, master=None):
        
        ttk.Frame.__init__(self, master)

        #------- Funcionaes

        self.Crear_Widgets_2()
    
    def Crear_Widgets_2(self):
        self.label3 = ttk.Label(self, text="B I E N V E N I D O").grid(row=0, column=0, sticky='NW', padx=190, pady=20)
        
        #------- Cuadro de Contenido
        self.canvas3 = tk.Canvas(self, height=450, width=470)
        self.canvas3.grid(column=0, row=0, sticky='NW', padx=0, pady=40)
        self.canvas3.create_rectangle(0, 10, 490, 0, outline="gainsboro") 
        
        #------- Cuadro de Texto
        self.text1 = tk.Text(self, width=0, height=0, bg="white", fg="black", padx=5, pady=5)
        self.text1.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text1.configure(cursor="arrow")


        #------- scroll bar
        ScrollBar1 = ttk.Scrollbar(self.text1, cursor="hand2")
        ScrollBar1.place(relheight=1, relx=0.950, rely=0)
        ScrollBar1.configure(command=self.text1.yview)

        #------- Mensaje de entrada TextBox
        self.mensaje1 = ttk.Entry(self, width=45)
        self.mensaje1.grid(row=1, column=0, sticky='NW', padx=100, pady=40, ipady=10)
        self.mensaje1.focus()
        self.mensaje1.bind("<Return>")

        #------- Boton de enviar
        self.button1_Enviar = ttk.Button(self, text="Enviar", width=9, cursor="hand2", command=lambda: self.Presionar(NONE)).grid(row=1, column=0, sticky='NW', padx=11, pady=40, ipady=9) 

        #------- Icono Buton Carpeta
        self.IconoImagen0 = Image.open('img/04.png')
        self.IconoImagen0 = self.IconoImagen0.resize((35, 35), Image.ANTIALIAS)
        self.IconoImagen0 = ImageTk.PhotoImage(self.IconoImagen0)
        self.ButtonIcono0 = ttk.Button(self, image=self.IconoImagen0, cursor="hand2", command = lambda: self.selectArchivo(NONE))
        self.ButtonIcono0.place(x=6, y=6)

        #------- Icono Buton MicroFono 
        self.IconoImagen = Image.open('img/01.png')
        self.IconoImagen = self.IconoImagen.resize((35, 35), Image.ANTIALIAS)
        self.IconoImagen = ImageTk.PhotoImage(self.IconoImagen)
        self.ButtonIcono = ttk.Button(self, image=self.IconoImagen, cursor="hand2", command = lambda: self.presionarAudio(NONE))
        self.ButtonIcono.place(x=409, y=570)

        #------- Label (Mostrando)
        self.labelMesanje = ttk.Label(self, text="Precione el boton para hablar")#.place(x=150, y=550)
        self.labelMesanje.grid(row=1, column=0, sticky='NW', padx=150, pady=10)

    def abrirArchivo(self):
        ruta = filedialog.askopenfilename(initialdir="/", title="Seleccione Archivo", filetypes=(("txt", "*.txt"),("all files","*.*")))
        print(ruta)
        shutil.copy(ruta, "article/archivo.txt")

    def selectArchivo(self, event):
        if os.path.isdir('article') == True:
            self.abrirArchivo()
        else:
            os.mkdir('article')
            self.abrirArchivo()

    def presionarAudio(self, event):
        #self.labelMesanje["text"] = "Procesando voz..."

        voz = ''
        r = sr.Recognizer()  
        with sr.Microphone() as source:
            #self.labelMesanje["text"] = "Procesando voz..."
            #print('Inicie la voz: ')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="es-US")
                voz = text
            except:
                self.labelMesanje["text"] = "Lo siento, no pude escucharle!................................"
                #print('Lo siento, no podemos escucharle')
        vozText = True
        self.InsertarMensaje(voz, "Tu", vozText)

        #self.labelMesanje["text"]="Presione de nuevo para hablar"
        #self.labelMesanje.destroy()
        #self.labelMesanje.grid_remove()

    def Presionar(self, event):
        sms = self.mensaje1.get()
        vozText = False
        self.InsertarMensaje(sms, "Tu", vozText)
    
    def respuestaT(self, texto):
        txt = Obtener_respuesta(texto)
        return txt  
    
    def respuestaV(self, voz):
        txt = Obtener_respuesta(voz)
        tts = gTTS(txt, lang='es-us')
        tts.save("audio01.mp3")
        playsound("audio01.mp3")
        remove("audio01.mp3")
        return txt

    def InsertarMensaje(self, sms, sender, vozText):

        if not sms:
            return
        
        #Entrayendo fecha
        self.Fecha = datetime.now().strftime("%d/%m/%Y-%X")

        self.mensaje1.delete(0, END)
        sms1 = f"{sender}: {sms}\n"
        self.text1.configure(state=NORMAL, font=("Verdana", 11), padx=10)
        self.text1.insert(END, self.Fecha + "\n" + sms1)
        self.text1.configure(state=DISABLED)

        self.mensaje1.delete(0, END)
    
        if vozText == True:
            mensaje = self.respuestaV(sms)
        elif vozText == False:
            mensaje = self.respuestaT(sms)

        sms2 = f"{Nombre_Bot}: {mensaje}\n\n"

        self.text1.configure(state=NORMAL)
        self.text1.insert(END, sms2)
        self.text1.configure(state=DISABLED)

        self.text1.see(END)
       
#-------------------------------------------
#            INTERFAZ
#-------------------------------------------

def main():
    
    ventana = Tk()
    ventana.title('The 4Fantastics')
    ventana.resizable(0,0) #Tamaño estatico
    ventana.iconbitmap("img/logo3.ico")
    ventana.geometry("470x650")
    
    #------- Preparando notebook (tabs)
    notebook = ttk.Notebook(ventana)
    notebook.pack(fill='both', expand='yes')#empaqueta el lienzo en un marco / formulario
    
    Pes1 = ttk.Frame(notebook)
    Pes2 = ttk.Frame(notebook)
    
    notebook.add(Pes1, text="Registrar Nombre")
    notebook.add(Pes2, text="Chat Bot")
    
    #------- Crear marcos de pestañas
    Pestana1 = Pestaña1(master=Pes1)
    Pestana1.grid()
    
    Pestana2 = Pestaña2(master=Pes2)
    Pestana2.grid()

    #------- Main loop
    ventana.mainloop()

if __name__ == '__main__':
    main()