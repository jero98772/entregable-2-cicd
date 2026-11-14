import pytest

pytestmark = pytest.mark.component


def test_restar_negativo_via_api(client):
    r = client.get("/restar", query_string={"a": 1, "b": 4})
    assert r.get_json()["resultado"] == -3


def test_respuesta_incluye_operacion(client):
    r = client.get("/multiplicar", query_string={"a": 2, "b": 5})
    assert r.get_json()["operacion"] == "multiplicar"
