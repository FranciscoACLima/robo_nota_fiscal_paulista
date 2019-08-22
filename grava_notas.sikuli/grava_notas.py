# -*- coding: utf-8 -*-
"""grava notas

Cadastra notas para a instituição CREN

Autor: Francisco A C Lima (faclsp@gmail.com)
"""
from sikuli import *
from configuracoes import *
from planilha import Planilha
# import nfp
# reload(nfp)
from nfp import Nfp


def main():
    mes_ref = definir_mes()
    nfp = Nfp('')
    plan = Planilha()
    n = 15000

    if not nfp.visualizar():
        msg = 'Pagina NF Paulista - campo chave não está visível'
        popError(msg.decode('utf-8'))
        exit()

    if not plan.visualizar():
        popError('Planilha não está aberta'.decode('utf-8'))
        exit()

    for i in range(n):
        codigo = ''
        # plan.irParaProximaLinha()
        if (i + 1) % 5 == 0:
            plan.gravar()
            sleep(3)
        plan.irParaProximaLinha()
        codigo = plan.capturarCelula()
        if not(codigo):
            popup('Célula Vazia'.decode('utf-8'))
            exit()
        nfp = Nfp(codigo)
        nfp.mes_ref = mes_ref
        nfp.visualizar()
        nfp.preencherFormulario()
        result = nfp.gravar()
        if result == 1:
            retorno = 'OK - gravado'
        elif result == 2:
            retorno = 'Nota Fiscal ja existe'
        elif result == 3:
            retorno = 'Nota Fiscal fora do prazo'
        elif result == 4:
            retorno = 'Codigo de barras invalido'
        else:
            retorno = 'Erro ao gravar nota'
        plan.visualizar()
        plan.retornarResultado(retorno)


def get_dia_atual():
    from datetime import datetime
    now = datetime.now()
    return now.day


def definir_mes():
    titulo = 'Gravar Nota Fiscal Paulista'
    texto = 'Escolha o mês de referência das notas'
    try:
        ult_opcao = Sikulix.prefLoad('ult_opcao', '')
    except Exception:
        ult_opcao = ''
    opcoes = (
        'Notas do mês anterior'.decode('utf-8'),
        'Notas deste mês'.decode('utf-8'),

    )
    selecionado = select(
        texto.decode('utf-8'),
        titulo.decode('utf-8'),
        opcoes,
        ult_opcao,
    )
    if selecionado is None:
        popError('Ação Cancelada!'.decode('utf-8'))
        exit()
    hoje = get_dia_atual()
    opcao = opcoes.index(selecionado)
    print(opcao, hoje)
    if opcao == 1 and hoje < 15:
        msg = "Você tem certeza que as notas fiscais são deste mês?"
        confirm = popAsk(msg.decode('utf-8'))
        if not confirm:
            exit(1)
    # Sikulix.prefStore('ult_opcao', selecionado)
    return opcao


# --------------------------------------------
if __name__ == "__main__":
    main()
