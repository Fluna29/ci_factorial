import pytest
from src.funciones import factorial

@pytest.mark.xfail(reason="Este test debe fallar intencionalmente")
def test_factorial_1_falla():
    assert factorial(0) == 1

def test_factorial_1_pasa():
    assert factorial(1) == 1

@pytest.mark.xfail(reason="Este test debe fallar intencionalmente")
def test_tipo_falla():
    with pytest.raises(TypeError):
        factorial('a')

def test_tipo_pasa():
    assert factorial(2) == 2

@pytest.mark.xfail(reason="Este test debe fallar intencionalmente")
def test_negativo_falla():
    with pytest.raises(ValueError):
        factorial(-1)

def test_negativo_pasa():
    assert factorial(2) == 2

@pytest.mark.xfail(reason="Este test debe fallar intencionalmente")
def test_positivo_falla():
    assert factorial(2) == 3

def test_positivo_pasa():
    assert factorial(2) == 2