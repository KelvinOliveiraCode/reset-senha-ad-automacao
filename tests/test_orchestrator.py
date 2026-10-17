"""Testes do orquestrador PasswordResetOrchestrator."""

from __future__ import annotations

from reset_senha_ad.models import ResetResult
from reset_senha_ad.orchestrator import PasswordResetOrchestrator


def test_reset_sucesso_retorna_resultado_com_ticket(fake_ad_client, ticket_generator) -> None:
    orchestrator = PasswordResetOrchestrator(fake_ad_client, ticket_generator)
    resultado = orchestrator.reset("jsilva", "NovaSenha123!")

    assert isinstance(resultado, ResetResult)
    assert resultado.success is True
    assert resultado.username == "jsilva"
    assert resultado.ticket is not None
    assert resultado.ticket.ticket_id == "AD-0001"
    assert resultado.message == "Senha redefinida com sucesso"
    assert fake_ad_client.calls == [("jsilva", "NovaSenha123!")]


def test_reset_falha_ad_ainda_gera_ticket(fake_ad_client, ticket_generator) -> None:
    fake_ad_client.should_fail = True
    resultado = PasswordResetOrchestrator(fake_ad_client, ticket_generator).reset(
        "jsilva", "NovaSenha123!"
    )

    assert resultado.success is False
    assert resultado.ticket is not None
    assert resultado.ticket.ticket_id == "AD-0001"
    assert resultado.message == "Falha no reset de senha"


def test_reset_rejeita_campos_vazios(fake_ad_client, ticket_generator) -> None:
    orchestrator = PasswordResetOrchestrator(fake_ad_client, ticket_generator)
    for username, senha in [("", "x"), ("jsilva", ""), ("   ", "x")]:
        try:
            orchestrator.reset(username, senha)
        except ValueError:
            continue
        raise AssertionError(f"esperava ValueError para username={username!r}")
