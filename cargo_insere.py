import pytest
from refere_calcular_conduzir import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_adicao(calc):
    assert calc.adicao(2, 3) == 5
    assert calc.adicao(-2, -3) == -5

def test_subtracao(calc):
    assert calc.subtracao(5, 3) == 2
    assert calc.subtracao(-5, -3) == -2

def test_multiplicacao(calc):
    assert calc.multiplicacao(2, 3) == 6
    assert calc.multiplicacao(-2, -3) == 6

def test_divisao(calc):
    assert calc.divisao(6, 3) == 2
    assert calc.divisao(5, 2) == 2.5
    with pytest.raises(ValueError):
        calc.divisao(5, 0)

def test_fatorial(calc):
    assert calc.fatorial(5) == 120
    assert calc.fatorial(0) == 1
    with pytest.raises(ValueError):
        calc.fatorial(-5)

def test_potencia(calc):
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(2, -3) == 0.125
