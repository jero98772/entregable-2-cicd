import pytest

from app import calculadora

pytestmark = pytest.mark.unit


def test_sumar_negativos():
    assert calculadora.sumar(-2, -3) == -5


def test_multiplicar_por_cero():
    assert calculadora.multiplicar(7, 0) == 0


def test_dividir_decimales():
    assert calculadora.dividir(1, 4) == pytest.approx(0.25)
