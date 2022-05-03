import board
from tkinter import *
import time

class gui:
    egerPX = 0
    egerPY = 0
    egerRX = 0
    egerRY = 0

    a = []

    def __init__(self):
        self.root = Tk()

        # Tábla beállítása
        self.szelesseg = 800
        self.magassag = 800
        self.kocka_meret = 80
        self.tarolo = Frame(self.root)
        self.tarolo.pack()

        # Tábla létrehozása
        self.tabla = Canvas(self.tarolo, width=self.szelesseg, height=self.magassag)
        self.tabla.pack()

        # Kockák létrehozása
        for i in range(8):
            for l in range(8):
                if l+i %2 == 0:
                    self.tabla.create_rectangle(i*self.kocka_meret, l*self.kocka_meret,
                                                self.kocka_meret*(i+1), self.kocka_meret*(l+1), fill="brown")
                else:
                    self.tabla.create_rectangle(i * self.kocka_meret, l*self.kocka_meret,
                                                self.kocka_meret * (i + 1), self.kocka_meret * (l + 1), fill="grey")

        self.root.after(10, self.rajz)
        self.root.mainloop()

    # Ha az egérrel klikkelünk valamelyik kockára akkor azt érzékelje
    def klikk(self,event):
        self.egerPX = int(event.y/self.kocka_meret)
        self.egerPY = int(event.x/self.kocka_meret)
        return

    # Egérrel ha érintjük valamelyik kockát
    def erintve(self,event):
        self.egerRX = event.y
        self.egerRY = event.x

        # Egér helyének megállapítása
        self.a = []
        self.a.append(self.egerPX, self.egerPY, int(self.egerRX/self.kocka_meret), int(self.egerRY/self.kocka_meret))
        # Meghatározás
        board.Tabla().meghatarozas(self.a)
        # Kocka rajzolás
        self.root.after(100, self.babuk())
        return

    # Bábuk felépítése
    def babuk(self):
        # Fehér Bábuk
        self.w.feher.bastya = PhotoImage(file= fehér.bástya.gif).subsample(4,4)
        self.w.feher.huszar = PhotoImage(file= fehér.huszár.gif).subsample(4,4)
        self.w.feher.futo = PhotoImage(file= fehér.futó.gif).subsample(4,4)
        self.w.feher.kiralyno = PhotoImage(file= fehér.királynő.gif).subsample(4,4)
        self.w.feher.kiraly = PhotoImage(file= fehér.király.gif).subsample(4,4)
        self.w.feher.gyalogos = PhotoImage(file= fehér.gyalogos.gif).subsample(4,4)
        # Fekete Bábuk
        self.w.fekete.bastya = PhotoImage(file= fekete.bástya.gif).subsample(4,4)
        self.w.fekete.huszar = PhotoImage(file= fekete.huszár.gif).subsample(4,4)
        self.w.fekete.futo = PhotoImage(file= fekete.futó.gif).subsample(4,4)
        self.w.fekete.kiralyno = PhotoImage(file= fekete.királynő.gif).subsample(4,4)
        self.w.fekete.kiraly = PhotoImage(file= fekete.király.gif).subsample(4,4)
        self.w.fekete.gyalogos = PhotoImage(file= fekete.gyalogos.gif).subsample(4,4)

        # Bábuk elhelyezése a táblán
        for i in range(64):
            #Fehér Bábuk
            if board.Board().sakk[int(i/8)][i%8] == "B":
                FBastya = self.w.create_image((i%8)*self.kocka_meret+2, int(i/8)*self.kocka_meret+2, anchor='nw', image=self.w.feher.bastya)
                self.w.cimke(FBastya, '<ButtonPress-1>', self.klikk)
                self.w.cimke(FBastya, '<ButtonRelease-1>', self.erintve)
            elif board.Board().sakk[int(i/8)][i%8] == "H":
                FHuszar = self.w.create_image((i%8)*self.kocka_meret+2, int(i/8*self.kocka_meret+2, anchor='nw', image=self.w.feher.huszar))
                self.w.cimke(FHuszar, '<ButtonPress-1>', self.klikk)
                self.w.cimke(FHuszar, '<ButtonRelease-1>', self.erintve)
            elif board.Board().sakk[int(i/8)][i%8] == "F":
                FFuto = self.w.create_image((i%8)*self.kocka_meret+2, int(i/8*self.kocka_meret+2, anchor='nw', image=self.w.feher.futo))
                self.w.cimke(FFuto, '<ButtonPress-1>', self.klikk)
                self.w.cimke(FFuto, '<ButtonRelease-1>', self.erintve)
            elif board.Board().sakk[int(i/8)][i%8] == "KŐ":
                FKiralyno = self.w.create_image((i%8)*self.kocka_meret+2, int(i/8*self.kocka_meret+2, anchor='nw', image=self.w.feher.kiralyno))
                self.w.cimke(FKiralyno, '<ButtonPress-1>', self.klikk)
                self.w.cimke(FKiralyno, '<ButtonRelease-1>', self.erintve)
            elif board.Board().sakk[int(i/8)][i%8] == "KY":
                FKiraly = self.w.create_image((i%8)*self.kocka_meret+2, int(i/8*self.kocka_meret+2, anchor='nw', image=self.w.feher.kiraly))
                self.w.cimke(FKiraly, '<ButtonPress-1>', self.klikk)
                self.w.cimke(FKiraly, '<ButtonRelease-1>', self.erintve)
            elif board.Board().sakk[int(i/8)][i%8] == "P":
                FGyalogos = self.w.create_image((i%8)*self.kocka_meret+2, int(i/8*self.kocka_meret+2, anchor='nw', image=self.w.feher.gyalogos))
                self.w.cimke(FGyalogos, '<ButtonPress-1>', self.klikk)
                self.w.cimke(FGyalogos, '<ButtonRelease-1>', self.erintve)
                #Fekete Bábuk
            elif board.Board().sakk[int(i/8)][i%8] == "b":
                BBastya = self.w.create_image((i%8)*self.kocka_meret+2, int(i/8*self.kocka_meret+2, anchor='nw', image=self.w.fekete.bastya))
                self.w.cimke(BBastya, '<ButtonPress-1>', self.klikk)
                self.w.cimke(BBastya, '<ButtonRelease-1>', self.erintve)
            elif board.Board().sakk[int(i/8)][i%8] == "h":
                BHuszar = self.w.create_image((i%8)*self.kocka_meret+2, int(i/8*self.kocka_meret+2, anchor='nw', image=self.w.fekete.huszar))
                self.w.cimke(BHuszar, '<ButtonPress-1>', self.klikk)
                self.w.cimke(BHuszar, '<ButtonRelease-1>', self.erintve)