"""Geracao deterministica de tickets de suporte."""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone

from .models import Ticket


class TicketGenerator:
    """Gera tickets com ID sequencial e deterministico."""

    def __init__(
        self,
        resolved_by: str,
        prefix: str = "AD",
        now: Callable[[], str] | None = None,
    ) -> None:
        self._resolved_by = resolved_by
        self._prefix = prefix
        self._counter = 0
        self._now = now or (lambda: datetime.now(timezone.utc).isoformat())

    def generate(self, username: str, action: str = "password_reset") -> Ticket:
        """Cria um ticket com ID sequencial (prefixo + contador de 4 digitos)."""
        self._counter += 1
        ticket_id = f"{self._prefix}-{self._counter:04d}"
        return Ticket(
            ticket_id=ticket_id,
            username=username,
            action=action,
            status="open",
            created_at=self._now(),
            resolved_by=self._resolved_by,
        )
