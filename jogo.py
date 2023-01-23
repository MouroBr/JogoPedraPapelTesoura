class Participante:
    def __init__(self):
        self.escolha = None
        self.ponto = 0
        self.chance = ""

    def escolha(self):
        self.escolha = input("{nome}, selecione Pedra, Papel ou Tesoura:".format(nome=self.nome))
        print("{nome} selects {chance}".format(nome=self.nome, chance=self.chance))


class Rodadas:
    def __init__(self, p1, p2):
        p1.escolha()
        p2.escolha()

    def compareEscolha(self):
        print("I")

    def pontos(self):
        print("")


class Jogo:
    def __init__(self):
        self.finalJogo = False
        self.participante01 = Participante("Carlos")
        self.participante02 = Participante("Anderson")
    def start(self):
        rodada = Rodadas(self.participante01, self.participante02)

    def checandoCondiçoes(self):
        print("")

    def determinaVencedor(self):
        print("")


game = Jogo()
game.start()
