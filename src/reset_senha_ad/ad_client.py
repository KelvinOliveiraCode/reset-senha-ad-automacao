"""Cliente de Active Directory para reset de senha."""

from __future__ import annotations

import os
import subprocess
from typing import Protocol, runtime_checkable


@runtime_checkable
class AdClient(Protocol):
    """Contrato de cliente AD: substitui-se por um fake em testes."""

    def reset_password(self, username: str, new_password: str) -> bool:
        """Redefine a senha do usuario no AD. Retorna True em caso de sucesso."""


class PowerShellAdClient:
    """Cliente AD real: executa o modulo ActiveDirectory via PowerShell 5.1."""

    def reset_password(self, username: str, new_password: str) -> bool:
        """Redefine a senha via Set-ADAccountPassword no PowerShell.

        Usuario e senha trafegam por variaveis de ambiente (nunca na linha de
        comando, que fica exposta na lista de processos do Windows).
        """

        command = (
            "$u = $env:AD_RESET_USER; "
            "$p = $env:AD_RESET_PASSWORD; "
            "$pwd = ConvertTo-SecureString -String $p -AsPlainText -Force; "
            "Set-ADAccountPassword -Identity $u -NewPassword $pwd -Reset"
        )
        env = os.environ.copy()
        env["AD_RESET_USER"] = username
        env["AD_RESET_PASSWORD"] = new_password
        cmd = [  # noqa: B607
            "powershell",
            "-NoProfile",
            "-Command",
            command,
        ]  # "powershell" e executavel padronizado do Windows
        try:
            result = subprocess.run(  # noqa: S603
                cmd,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            return result.returncode == 0
        except (OSError, subprocess.SubprocessError):
            return False
