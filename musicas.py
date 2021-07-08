'''BOMusic'''
from tkinter import *
from musica1 import App
from musica2 import App2
from musica3 import App3

class Musicas(Toplevel):
 #-----------------TELA 2-------------------------
    cor1 = '#000100'
    cor2 = '#58009D'
    cor3 = '#171717'
    cor4 = '#efefef'
 
    def __init__(self, original):
 
        self.frame_original = original
        Toplevel.__init__(self)    

        self.config()
        self.texto()
        self.frames()
        self.botoes()
 
    def config(self):
        self.title('BOMusic')
        self.geometry('380x380+700+350')
        self.resizable(False, False)
        self.configure(bg = self.cor3)
        self.iconbitmap('provaDevSistemas\icone.ico')

    def clickbtn(self):
        self.withdraw()
        self.subFrame = App(self)

    def clickbtn2(self):
        self.withdraw()
        self.subFrame = App2(self)

    def clickbtn3(self):
        self.withdraw()
        self.subFrame = App3(self)

    def frames(self):
        self.album1 = Frame(
            self,
            bg = self.cor4,
        )

        self.album1.place(
            x = 10,
            y = 110,
            width = 75,
            height = 75
        )

        self.album2 = Frame(
            self,
            bg = self.cor4,
        )

        self.album2.place(
            x = 10,
            y = 200,
            width = 75,
            height = 75
        )

        self.album3 = Frame(
            self,
            bg = self.cor4,
        )

        self.album3.place(
            x = 10,
            y = 290,
            width = 75,
            height = 75
        )

    def texto(self):
        Label(self, text = 'Playlist', font = ('Poppins Bold', 25), background= '#171717', fg = self.cor2).place(x= 119, y=20)
        Label(self, text = 'Olivia Rodrigo - good 4 u', font = 'Poppins', background= '#171717', fg = self.cor2).place(x=90, y=130)
        Label(self, text = 'CMK, Knust, Azzy - Antes de Partir', font = 'Poppins', background= '#171717', fg = self.cor2).place(x=90, y=220)
        Label(self, text = 'Twenty One Pilots - Shy Away', font = 'Poppins', background= '#171717', fg = self.cor2).place(x=90, y=310)

#    def imgBtn(self):

    def show(self):
        self.update()
        self.deiconify()


    def botoes(self):

        self.imgbtn1 = PhotoImage(file = 'provaDevSistemas\imgbtn1.png')

        self.botao1 = Button(
            self.album1,
            image = self.imgbtn1,
            command = self.clickbtn
        )

        self.botao1.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )

        ###################

        self.imgbtn2 = PhotoImage(file = 'provaDevSistemas\imgbtn2.png')

        self.botao2 = Button(
            self.album2,
            image = self.imgbtn2,
            command = self.clickbtn2
        )

        self.botao2.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )
        ###################

        self.imgbtn3 = PhotoImage(file = 'provaDevSistemas\imgbtn3.png')

        self.botao3 = Button(
            self.album3,
            image = self.imgbtn3,
            command=self.clickbtn3
        )

        self.botao3.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )