# -*- coding: utf-8 -*-
"""nfp

Controla a tela da nota fiscal paulista

Autor: Francisco A C Lima (faclsp@gmail.com)
"""
from sikuli import *
from tela import Tela


class Nfp(Tela):
    """Classe Nfp

    Representa uma tela da Nota Fiscal

    Extends:
        Tela
    """
    icone = "icone_nav.png"
    imgLogin = "img_login.png"
    imagemPadrao = "cmp_chave.png"
    pagInic = "pag_inic.png"

    def __init__(self, codigo):
        """Init

        Construtor da Classe Nfp
        """
        self.codigo = codigo
        self.mesRef = 0
        self.aplicativo = aplicativo
        self.aplicativoCmd = aplicativo_cmd

    @property
    def mesAtual(self):
        from datetime import datetime
        now = datetime.now()
        return now.month

    def preencherFormulario(self):
        codigo = self.codigo
        cmp_chave = Pattern("cmp_chave.png")
        if not exists(cmp_chave, 15):
            self._reiniciar()
            return
        click(cmp_chave.targetOffset(203, 3))
        sleep(1)
        type(Key.DELETE)
        paste(codigo)
        sleep(1)

    def gravar(self):
        type(Key.ENTER)
        sleep(2)
        gravado = "gravado.png"
        if exists(gravado, 15):
            # if exists(cmp_limpo):
            return 1
        ja_existe = "ja_existe.png"
        if exists(ja_existe):
            return 2
        fora_do_prazo = "fora_do_prazo.png"
        if exists(fora_do_prazo):
            return 3
        codigo_invalido = "codigo_invalido.png"
        if exists(codigo_invalido):
            return 4
        codigo_nao_digitado = "codigo_nao_digitado.png"
        if exists(codigo_nao_digitado):
            return 5
        if exists("req_nao_atendida.png"):
            sleep(120)
            self._reabrir()
            try:
                self._reiniciar()
                return self.gravar()
            except Exception:
                self._reabrir()
        if exists(self.pagInic):
            if self._reiniciar():
                return self.gravar()
            else:
                self._reabrir()
                self._reiniciar(True)
                return self.gravar()

    def _reabrir(self, tentativa=0):

        tentativa += 1
        Debug.user('Reabrir - tentativa ' + str(tentativa))
        linha_url = "linha_url.png"
        click(linha_url)
        type(Key.ENTER)
        if exists(self.pagInic, 10):
            return
        if exists("entidades.png", 2):
            return
        if tentativa < 20:
            sleep(10)
            if exists("req_nao_atendida.png"):
                sleep(120)
            return self._reabrir(tentativa)
        popError('Favor Logar novamente')
        exit()

    def _reiniciar(self, prosseguir=True):
        if prosseguir:
            entidades = "entidades.png"
            if not exists(entidades):
                return False
            for i in range(4):
                hover(entidades)
                sleep(1)
                cad_cupons = "cad_cupons.png"
                if exists(cad_cupons, 3):
                    click(cad_cupons)
                    break
        img = "prosseguir.png"
        if not(exists(img, 20)):
            return self._reabrir()
        for i in range(4):
            if exists(img):
                click(img)
                sleep(2)
        # click(img)
        img = Pattern("escolh_entidade.png")
        if not(exists(img, 20)):
            return False
        click(img.targetOffset(191, -1))
        sleep(1)
        type(Key.DOWN)
        type(Key.ENTER)
        sleep(2)
        Debug.info('mesRef: ' + str(self.mesRef))
        if self.mesRef != 1:  # mes anterior
            mesAtual = self.mesAtual
            img = Pattern("data_da_nota.png")
            click(img.targetOffset(170, 0))
            sleep(1)
            type(Key.UP)
            type(Key.ENTER)
            sleep(1)
            if mesAtual == 1:
                img = Pattern("img_ano.png").similar(0.75)
                click(img.targetOffset(45, 0))
                sleep(1)
                type(Key.DOWN)
                type(Key.ENTER)
                sleep(1)
        nova_nota = "nova_nota.png"
        click(nova_nota)
        sleep(1)
        self._confirmarMsg()
        self.preencherFormulario()
        return True

    def _confirmarMsg(self):
        img = Pattern("nfp_msg.png")
        sleep(1)
        if exists(img):
            click(img.targetOffset(206, 3))
            sleep(2)


# --------------------------------------------#
#             Testes do módulo nfp            #
# --------------------------------------------#

class TestesTela(object):

    def visualizaNfp(self):
        tela = Nfp('')
        tela.visualiza()
        if tela.estaAberta():
            popup('OK navegador Aberto')
            sleep(3)

    def reiniciarMesAnterior(self):
        tela = Nfp('')
        tela.mesRef = 0
        tela._reiniciar()

    def reiniciarMesAtual(self):
        tela = Nfp('')
        tela.mesRef = 1
        tela._reiniciar()

    def capturaMesAtual(self):
        tela = Nfp('')
        print(tela.mesAtual)


# ------------------------------------------------------------------------#
if __name__ == "__main__":
    from configuracoes import *
    teste = TestesTela()
    teste.visualizaNfp()
