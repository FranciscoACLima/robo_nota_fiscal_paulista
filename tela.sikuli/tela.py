# -*- coding: utf-8 -*-
"""tela

Controla uma tela qualquer do Sistema Operacional. A partir desta classe
parte toda a automatização.

Autor: Francisco A C Lima (faclsp@gmail.com)
"""
from sikuli import *


class Tela(object):
    """Classe Tela """

    botaoFechar = ''
    sleepDefault = 0.5
    aplicativo = ''

    def __init__(self):
        """Init

        Construtor da Classe Tela
        """
        self.icone = ''
        self.imagemPadrao = ''

    def abrir(self, tentativa=1):
        self._confereIconePadrao()
        click(self.icone)
        if not self.estaAberta() and tentativa == 1:
            self.abrir(0)
        if self.estaAberta():
            return True
        return False

    def estaAberta(self, time=10):
        sleep(1)
        if exists(self.imagemPadrao, time):
            return True
        return False

    def visualizar(self, tentativa=1):
        self._confereIconePadrao()
        click(self.icone)
        # hover(Pattern(self.icone).targetOffset(0, -200))
        if not self.estaAberta() and tentativa == 1:
            self.visualizar(0)
        if self.estaAberta():
            hover(Location(653, 884))
            return True
        return False

    def _confereIconePadrao(self):
        if not exists(self.icone):
            msg = "Icone para abrir/visualizar \"{}\" não encontrado!".format(self.aplicativo)
            msg = msg.decode('utf-8')
            popError(msg)
            raise Exception(msg)


# --------------------------------------------#
#           Testes da Classe Tela             #
# --------------------------------------------#
class TestesTela():
    pass


if __name__ == "__main__":
    pass
