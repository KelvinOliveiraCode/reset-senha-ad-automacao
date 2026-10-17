"""Interface de linha de comando para reset de senha AD."""

from __future__ import annotations

import argparse
import sys

from .ad_client import PowerShellAdClient
from .models import ResetResult
from .orchestrator import PasswordResetOrchestrator
from .ticket import TicketGenerator


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="reset-senha-ad",
        description=(
            "Redefine a senha de um usuario no Active Directory e gera um ticket de suporte."
        ),
    )
    parser.add_argument("username", help="Login do usuario no AD (sAMAccountName)")
    parser.add_argument("new_password", help="Nova senha do usuario")
    parser.add_argument(
        "--resolved-by",
        default="suporte-ti",
        help="Identificador de quem executa o reset (padrao: suporte-ti)",
    )
    args = parser.parse_args(argv)

    orchestrator = PasswordResetOrchestrator(
        ad_client=PowerShellAdClient(),
        ticket_generator=TicketGenerator(resolved_by=args.resolved_by),
    )
    try:
        result: ResetResult = orchestrator.reset(args.username, args.new_password)
    except ValueError as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 2

    print(f"ticket: {result.ticket.ticket_id}")
    print(f"usuario: {result.username}")
    print(f"sucesso: {result.success}")
    print(f"mensagem: {result.message}")
    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
