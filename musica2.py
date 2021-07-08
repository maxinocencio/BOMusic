'''BOMusic'''

#https://github.com/maxinocencio/BOMusic

from tkinter import *       #importando bibliotecas
import pygame               #importando bibliotecas

class App2(Toplevel):

    cor1 = '#171717'
    cor2 = '#58009D'        #variantes de cores
    cor3 = '#efefef'

    def __init__(self, original):

        self.frame_original = original
        Toplevel.__init__(self)      
        
        self.config()
        self.frames()
        self.widgetsButton1()
        self.widgetsButton2()           #aplicando funções no app
        self.widgetsButton3()
        self.widgetsimg()
        self.widgetstitulo()

    def config(self):
        self.title('BoMusic')
        self.geometry('380x380+700+350')            #configurando geometria e configurações
        self.resizable(False, False)
        self.configure(bg = self.cor1)
        pygame.mixer.init()
        self.iconbitmap('icone.ico')

    def som(self):
        pygame.mixer.music.load('musica2.mp3')         #função de iniciar música
        pygame.mixer.music.play()
        StopIteration

        print('tocando')
        print('')

    def stop(self):
        pygame.mixer.music.pause()          #função de parar música
        print('parando')
        print('')
        StopIteration

    def clickbtn(self):
        self.withdraw()
        #self.subFrame = Musicas(self)      #função de pausar música
        self.stop()

    def onClose(self):
        self.stop()
        self.destroy()
        self.frame_original.show()          #função de voltar

    def frames(self):
        self.titulo = Frame(            # até linha 117 criando e colocando frames
            self,
            bg = self.cor1,
        )

        self.titulo.place(
            x = 0,
            y = 20,
            width = 380,
            height = 100
        )

        self.logo = Frame(
            self,
            bg = self.cor1,
        )

        self.logo.place(
            x = 0,
            y = 140,
            width = 380,
            height = 100
        )

        self.voltar = Frame(
            self,
            bg = self.cor3,
        )

        self.voltar.place(
            x = 12.5,
            y = 280,
            width = 110,
            height = 50
        )

        self.play = Frame(
            self,
            bg = self.cor1,
        )

        self.play.place(
            x = 135,
            y = 280,
            width = 110,
            height = 50
        )

        self.parar = Frame(
            self,
            bg = self.cor3,
        )

        self.parar.place(
            x = 257.5,
            y = 280,
            width = 110,
            height = 50
        )

    def widgetstitulo(self):
        title = Label(self.titulo,
            text='CMK, Knust, Azzy\nAntes de Partir',           #colocando título na música
            font=('Poppins', 20, 'bold'),
            bg = self.cor1,
            fg = self.cor2,
        )
        title.pack()

    def widgetsimg(self):
        self.album = PhotoImage(file = 'album2.png')      #colocando foto do álbum
        self.img2 = Label(
            self.logo,
            image = self.album,
            bd = 0
        )
        self.img2.pack()                #posicionando foto de álbum

    def widgetsButton1(self):
        self.botao3 = Button(
            self.voltar,
            text = 'Voltar',
            font = ('Poppins', 25),             #criando botão de voltar
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.onClose
        )

        self.botao3.place(                  #posicionando botão de voltar
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        ) 

    def widgetsButton2(self):
        self.botao = Button(
            self.play,
            text = 'Play',                  #colocando botão de iniciar
            font = ('Poppins', 25),
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.som
        )

        self.botao.place(               #posicionando botão de colocar
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )     
        
    def widgetsButton3(self):
        self.botao2 = Button(
            self.parar,
            text = 'Stop',              #colocando botão de pausar
            font = ('Poppins', 25),
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.stop
        )

        self.botao2.place(          #posicionando botão de pausar
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )
