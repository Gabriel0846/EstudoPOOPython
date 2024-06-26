class Televisor:

    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20

    def aumentaVolume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuiVolume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocaCanal(self, canal):
        if canal in self.lista_de_canais:
            self.canal_atual = canal

    def sintonizaCanal(self, canal):
        self.lista_de_canais.append(canal)

