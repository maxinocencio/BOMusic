from tkinter import * # importando bibliotecas.
import pygame          # importando bibliotecas.

from musica1 import App         
from musicas import Musicas

class Inicio():
    cor1 = '#171717'
    cor2 = '#58009D'    #variáveis de cores
    cor3 = '#efefef'

    def __init__(self):
        self.root = root
        
        self.config()
        self.frames()
        self.widgetsButton()            #aplicando alterações
        self.widgetstitulo()
        self.widgetsimg()

        root.mainloop()

    def config(self):
        self.root.title('BoMusic')
        self.root.geometry('380x380+700+350')           #configurando layout e geometria do app
        self.root.resizable(False, False)
        self.root.configure(bg = self.cor1)
        pygame.mixer.init()
        self.root.iconbitmap('provaDevSistemas\icone.ico')

    def hide(self):
        self.root.withdraw()

    def clickbtn(self):
        self.hide()                         #criando botão voltar
        self.subFrame = Musicas(self)

    def frames(self):
        self.titulo = Frame(
            self.root,                      #criando frames
            bg = self.cor1,
        )

        self.titulo.place(                  #posicionando frames
            x = 0,
            y = 20,
            width = 380,
            height = 100
        )

        self.logo = Frame(
            self.root,
            bg = self.cor3,
        )

        self.logo.place(
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
            text='BOMusic',
            font=('Poppins', 35, 'bold'),       #criando título
            bg = self.cor1,
            fg = self.cor2,
        )
        title.place(rely = 0.06, relx = 0.22)

    def widgetsimg(self):
        self.fone = PhotoImage(file = 'provaDevSistemas\logo.png')      #aplicando foto de titulo
        self.img = Label(
            self.logo,
            image = self.fone,
            bd = 0
        )
        self.img.pack()                             #posicionando foto 

    def widgetsButton(self):
        self.botao = Button(
            self.play,
            text = 'Entrar',
            font = ('Poppins', 25),
            fg = self.cor3,                 #criando botão de entrada e posicionando
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.clickbtn
        )

        self.botao.place(
            x = 102.5,
            y = 12.5,
            width = 175,
            height = 75
        ) 
        
root = Tk()                     #programa principal
Inicio()
