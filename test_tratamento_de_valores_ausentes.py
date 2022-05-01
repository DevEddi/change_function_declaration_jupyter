import pytest
from testbook import testbook
import pandas as pd

data_test= pd.read_csv('mamografia.csv')


@testbook('./tratamento_de_valores_ausentes.ipynb', execute=True)
def test_tratar_ausentes(tb):
    tratar_ausentes = tb.ref("tratar_ausentes")
    lista = ['BI-RADS', 'Idade', 'Forma', ' Margem', ' Densidade', 'Severidade']
    assert tratar_ausentes(lista) == None

@testbook('./tratamento_de_valores_ausentes.ipynb', execute=True)
def test_verifica_moda_da_severidade_zero(tb):
    moda_severidade = tb.ref("verifica_moda_da_severidade")
    lista = data_test.columns
    moda_benigno = data_test[(data_test['Severidade'] == 0)][lista].mode()[0]
    data_test.loc[(data_test[lista].isnull()) & (data_test['Severidade'] == 0), lista] = moda_benigno
    assert moda_severidade(lista) == None

