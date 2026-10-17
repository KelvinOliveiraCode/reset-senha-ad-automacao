"""Testes da geracao deterministica de tickets de suporte."""

from __future__ import annotations


def test_gera_ticket_com_id_sequencial_e_status_aberto(ticket_generator) -> None:
    ticket = ticket_generator.generate("jsilva")

    assert ticket.ticket_id == "AD-0001"
    assert ticket.username == "jsilva"
    assert ticket.action == "password_reset"
    assert ticket.status == "open"
    assert ticket.created_at == "2026-10-16T12:00:00+00:00"
    assert ticket.resolved_by == "suporte-ti"


def test_ids_sao_unicos_e_sequenciais(ticket_generator) -> None:
    ids = [ticket_generator.generate(f"user{i}").ticket_id for i in range(5)]

    assert ids == ["AD-0001", "AD-0002", "AD-0003", "AD-0004", "AD-0005"]
