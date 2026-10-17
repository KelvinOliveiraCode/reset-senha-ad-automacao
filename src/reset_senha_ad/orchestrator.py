"""Orquestrador: reset de senha no AD mais geracao de ticket de suporte."""

from __future__ import annotations

from .ad_client import AdClient
from .models import ResetResult
from .ticket import TicketGenerator


class PasswordResetOrchestrator:
    """Coordena o reset de senha e a geracao do ticket de suporte."""

    def __init__(
        self, ad_client: AdClient, ticket_generator: TicketGenerator
    ) -> None:
        self._ad_client = ad_client
        self._ticket_generator = ticket_generator

    def reset(self, username: str, new_password: str) -> ResetResult:
        """Executa o reset de senha e gera o ticket correspondente.

        O ticket eh gerado mesmo quando o reset falha para manter o rastro
        da tentativa na fila de suporte.
        """
        if not username or not username.strip():
            raise ValueError("username e obrigatorio")
        if not new_password or not new_password.strip():
            raise ValueError("new_password e obrigatorio")

        success = self._ad_client.reset_password(username, new_password)
        ticket = self._ticket_generator.generate(username)
        message = (
            "Senha redefinida com sucesso" if success else "Falha no reset de senha"
        )
        return ResetResult(
            success=success,
            username=username,
            ticket=ticket,
            message=message,
        )
