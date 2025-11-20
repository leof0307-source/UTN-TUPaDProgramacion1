# d) Polimorfismo

class Ave:
    def volar(self):
        print("El ave está volando.")

class Pinguino(Ave):
    def volar(self):
        print("El pingüino no puede volar, pero puede nadar.")

def hacer_volar(ave):
    ave.volar()

pajaro = Ave()
pinguino = Pinguino()

hacer_volar(pajaro)
hacer_volar(pinguino)