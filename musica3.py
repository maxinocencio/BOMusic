'''BOMusic'''

from tkinter import *
import pygame

class App3(Toplevel):

    cor1 = '#171717'
    cor2 = '#58009D'
    cor3 = '#efefef'

    def __init__(self, original):

        self.frame_original = original
        Toplevel.__init__(self)      
        
        self.config()
        self.frames()
        self.widgetsButton()
        self.widgetsButton2()
        self.widgetsimg()
        self.widgetstitulo()
        self.widgetsButton3()

    def config(self):
        self.title('BoMusic')
        self.geometry('380x380+700+350')
        self.resizable(False, False)
        self.configure(bg = self.cor1)
        pygame.mixer.init()
        self.iconbitmap('provaDevSistemas\icone.ico')

    def som(self):
        pygame.mixer.music.load('provaDevSistemas\musica3.mp3')
        pygame.mixer.music.play()
        StopIteration

        print('tocando')
        print('')

    def stop(self):
        pygame.mixer.music.pause()
        print('parando')
        print('')
        StopIteration

    def clickbtn(self):
        self.withdraw()
        #self.subFrame = Musicas(self)
        self.stop()

    def frames(self):
        self.titulo = Frame(
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

        self.play = Frame(
            self,
            bg = self.cor1,
        )

        self.play.place(
            x = 12.5,
            y = 280,
            width = 110,
            height = 50
        )

        self.parar = Frame(
            self,
            bg = self.cor3,
        )

        self.parar.place(
            x = 135,
            y = 280,
            width = 110,
            height = 50
        )

        self.voltar = Frame(
            self,
            bg = self.cor3,
        )

        self.voltar.place(
            x = 257.5,
            y = 280,
            width = 110,
            height = 50
        )

    def widgetstitulo(self):
        title = Label(self.titulo,
            text='Twenty One Pilots\nShy Away',
            font=('Poppins', 20, 'bold'),
            bg = self.cor1,
            fg = self.cor2,
        )
        title.pack()

    def widgetsimg(self):
        self.album = PhotoImage(file = r'provaDevSistemas\album3.png')
        self.img2 = Label(
            self.logo,
            image = self.album,
            bd = 0
        )
        self.img2.pack()

    def widgetsButton(self):
        self.botao = Button(
            self.play,
            text = 'Play',
            font = ('Poppins', 25),
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.som
        )

        self.botao.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )     
        
    def widgetsButton2(self):
        self.botao2 = Button(
            self.parar,
            text = 'Stop',
            font = ('Poppins', 25),
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.stop
        )

        self.botao2.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )

    def widgetsButton3(self):
        self.botao3 = Button(
            self.voltar,
            text = 'Voltar',
            font = ('Poppins', 25),
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.clickbtn
        )

        self.botao3.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        ) 