class Dars:
    def __init__(self, nomi, soat):
        self.nomi = nomi
        self.soat = soat

    def oshir(self, n):
        self.soat += n
        print(f"{n} soat qo‘shildi")

    def kamaytir(self, n):
        self.soat -= n
        print(f"{n} soat kamaydi")

    def info(self):
        print(f"Dars: {self.nomi}")
        print(f"Soat: {self.soat}")


d1 = Dars("Matematika", 2)

d1.info()
d1.oshir(1)
d1.kamaytir(1)
d1.info()
