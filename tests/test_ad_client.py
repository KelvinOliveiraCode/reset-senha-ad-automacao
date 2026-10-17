"""Testes do cliente AD falso e do contrato AdClient."""

from __future__ import annotations

from reset_senha_ad.ad_client import AdClient


def test_reset_password_sucesso_grava_chamada(fake_ad_client) -> None:
    resultado = fake_ad_client.reset_password("jsilva", "NovaSenha123!")

    assert resultado is True
    assert fake_ad_client.calls == [("jsilva", "NovaSenha123!")]


def test_reset_password_falha_grava_chamada_mesmo_assim(fake_ad_client) -> None:
    fake_ad_client.should_fail = True
    resultado = fake_ad_client.reset_password("jsilva", "NovaSenha123!")

    assert resultado is False
    assert fake_ad_client.calls == [("jsilva", "NovaSenha123!")]


def test_fake_ad_client_satise_o_protocolo_ad_client(fake_ad_client) -> None:
    assert isinstance(fake_ad_client, AdClient)
