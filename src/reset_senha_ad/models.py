"""Modelos de dominio do reset de senha do Active Directory."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Ticket:
    """Ticket de suporte gerado apos um reset de senha."""

    ticket_id: str
    username: str
    action: str
    status: str
    created_at: str
    resolved_by: str


@dataclass(frozen=True)
class ResetResult:
    """Resultado da operacao combinada reset de senha + ticket de suporte."""

    success: bool
    username: str
    ticket: Ticket | None
    message: str
