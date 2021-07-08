from tkinter import * # importando bibliotecas
import pygame          # importando bibliotecas

from musica1 import App  #importando classes
from musicas import Musicas 

class Inicio():
    cor1 = '#171717'           
    cor2 = '#58009D'    #variáveis de cores
    cor3 = '#efefef'

    def __init__(self):
        self.root = root
        
        self.config()
        self.frames()
        self.widgetsButton()        #aplicação de configurações do layout
        self.widgetstitulo()
        self.widgetsimg()

        root.mainloop()

    def config(self):
        self.root.title('BoMusic')
        self.root.geometry('380x380+700+350')       # configuração de layout
        self.root.resizable(False, False)
        self.root.configure(bg = self.cor1)
        pygame.mixer.init()
        self.root.iconbitmap('provaDevSistemas\icone.ico')

    def hide(self):
        self.root.withdraw()    #funções 

    def clickbtn(self):
        self.hide()                 #funções
        self.subFrame = Musicas(self)

    def frames(self):
        self.titulo = Frame(
            self.root,              #funções frames
            bg = self.cor1,
        )

        self.titulo.place(
            x = 0,
            y = 20,                    #posicionando
            width = 380,
            height = 100
        )

        self.logo = Frame(
            self.root,
            bg = self.cor3,
        )

        self.logo.place(                        #posicionando widgets
            x = 140,
            y = 140,
            width = 100,
            height = 100
        )

        self.play = Frame(
            self.root,
            bg = self.cor1,
        )

        self.play.place(
            x = 0,
            y = 260,
            width = 380,
            height = 100
        )
        
    def widgetstitulo(self):
        title = Label(self.titulo,
            text='BOMusic',                         #criando widgets
            font=('Poppins', 35, 'bold'),
            bg = self.cor1,
            fg = self.cor2,
        )
        title.place(rely = 0.06, relx = 0.22)           #posicionando widgets

    def widgetsimg(self):
        self.fone = PhotoImage(file = 'provaDevSistemas\logo.png')
        self.img = Label(
            self.logo,
            image = self.fone,
            bd = 0
        )
        self.img.pack()                                          #posicionando widgets

    def widgetsButton(self):
        self.botao = Button(
            self.play,
            text = 'Entrar',
            font = ('Poppins', 25),
            fg = self.cor3,                                           #criando widgets
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.clickbtn
        )

        self.botao.place(
            x = 102.5,
            y = 12.5,                                                  #posicionando widgets
            width = 175,
            height = 75
        ) 
            
root = Tk()
Inicio()                                                            #programa principal
