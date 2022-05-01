import pytest
from testbook import testbook

@testbook('./tratamento_de_valores_ausentes.ipynb', execute=True)
def test_retorna_substituicao_valores_ausentes(tb):
    tratar_ausentes = tb.ref("tratar_ausentes")
    lista = ['BI-RADS', 'Idade', 'Forma', ' Margem', ' Densidade', 'Severidade']
    assert tratar_ausentes(lista) == None

@testbook('./tratamento_de_valores_ausentes.ipynb', execute=True)
def test_retorna_substituicao_pela_moda(tb):
    moda_severidade = tb.ref("verifica_moda_da_severidade")
    lista = ['BI-RADS', 'Forma', ' Margem', ' Densidade', 'Severidade']
    for lis in lista:
        assert moda_severidade(lis) == None


@testbook('./tratamento_de_valores_ausentes.ipynb', execute=True)
def test_retorna_substituicao_pela_media(tb):
    media_severidade = tb.ref("verifica_media_da_severidade")
    assert media_severidade('Idade') == None


