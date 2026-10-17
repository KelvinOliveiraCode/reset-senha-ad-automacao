"""Fixtures e doubles compartilhados pela suíte de testes."""

from __future__ import annotations

import pytest

from reset_senha_ad.ad_client import AdClient
from reset_senha_ad.ticket import TicketGenerator


class FakeAdClient(AdClient):
    """Cliente AD falso: grava chamadas e devolve resultado controlado."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []
        self.should_fail = False

    def reset_password(self, username: str, new_password: str) -> bool:
        self.calls.append((username, new_password))
        return not self.should_fail


def fixed_now() -> str:
    """Carimbo de data/hora fixo para testes determinísticos."""
    return "2026-10-16T12:00:00+00:00"


@pytest.fixture
def fake_ad_client() -> FakeAdClient:
    return FakeAdClient()


@pytest.fixture
def ticket_generator() -> TicketGenerator:
    return TicketGenerator(resolved_by="suporte-ti", now=fixed_now)
