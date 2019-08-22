# -*- coding: utf-8 -*-
"""planilha

Controla uma planilha do excel. Atualmente trabalhando
apenas com o Excel 2010.

Esta classe serve para entrada de dados, normalmente uma lista de
processos que serão trabalhados, e também para gravar o resultado
da da tarefa executada pelo robô.


Autor: Francisco A C Lima (franciscol@tjsp.jus.br)
"""
from sikuli import *
from tela import Tela


class Planilha(Tela):
    """Classe Planilha

    Classe que controla a entrada de dados para os robôs a partir
    de uma planilha, bem como o retorno da tarefa executada.
    """

    aplicativo = 'Planilha'

    def __init__(self):
        """Construtor da Classe

        Verifica ao carregar o objeto se a planilha está aberta
        """
        self.icone = "icone_plan.png"
        self.imagemPadrao = "img_plan.png"

    def capturarCelula(self, coluna=0):
        """captura Celula

        Keyword Arguments:
            coluna {number} -- número da coluna (default: {0})

        Returns:
            str -- texto capturado
        """
        # Env.setClipboard('')
        if coluna:
            type(Key.HOME)
            for i in range(0, coluna):
                type(Key.RIGHT)
        sleep(1)
        type('c', KeyModifier.CTRL)
        sleep(1)
        texto = Env.getClipboard()
        texto = texto.strip()
        sleep(1)
        return texto

    def gravar(self):
        """grava

        Grava a planilha a cada alteração

        Returns:
            bol -- True se a planilha foi gravada
        """
        sleep(1)
        type('s', KeyModifier.CTRL)
        sleep(2)
        return True

    def retornarResultado(self, resultado):
        """retorna resultado

        Retorna na planilha o resultado da análise ou tarefa executada.

        Arguments:
            resultado {str} -- texto de retorno

        Returns:
            bool -- True se o resultado for inserido
        """
        self.irParaProximaCelula()
        sleep(1)
        # Debug.log('resultado: ' + resultado)
        resultado = resultado.strip()
        resultado = resultado.replace('?', '')
        resultado = resultado.replace('`', '\'')
        resultado = resultado.replace('/', Key.DIVIDE)
        paste(resultado)
        sleep(1)
        return True

    def irParaProximaCelula(self):
        sleep(0.5)
        type(Key.RIGHT)

    def irParaProximaLinha(self):
        type(Key.HOME)
        type(Key.DOWN)


# --------------------------------------------#
#          Testes da Classe Planilha          #
# --------------------------------------------#
class TestesTela():

    def capturaRetornaResultado(self):
        planilha = Planilha()
        planilha.visualizar()
        texto = planilha.capturarCelula()
        # texto = texto.replace('\n', '_')
        print('** ' + texto + ' **')
        planilha.retornarResultado(texto)
        planilha.irParaProximaCelula()


# ----------------------------------------------
if __name__ == "__main__":
    teste = TestesTela()
    teste.capturaRetornaResultado()
