# reset-senha-ad-automacao

Automacao de reset de senha do Active Directory com geracao de ticket de suporte — area Suporte TI.

## Descricao / Description

**PT-BR:** Pacote PowerShell + Python que redefine a senha de um usuario no Active Directory (modulo ActiveDirectory) e gera um ticket de suporte numerado de forma sequencial e deterministica. Escopo do MVP: reset de senha + geracao de ticket.

**EN:** PowerShell + Python package that resets an Active Directory user password (ActiveDirectory module) and generates a numbered support ticket, sequentially and deterministically. MVP scope: password reset + ticket generation.

## Stack

PowerShell 5.1, Python 3.10+. Nenhuma dependencia externa.

## Como usar / How to use

### Pre-requisitos

- Windows com PowerShell 5.1 e o modulo ActiveDirectory (RSAT) instalado.
- Permissao para redefinir senhas no AD.

### Com o PowerShell (recomendado para uso direto no suporte)

**PT-BR:**

```
.\src\Reset-SenhaAD.ps1 -Username jsilva -NewPassword "N0vaSenha123!"
```

Saída esperada:

```
SUCESSO: senha redefinida para jsilva
TICKET: AD-jsilva-20261016-120000
```

**EN:**

```
.\src\Reset-SenhaAD.ps1 -Username jsilva -NewPassword "N0vaSenha123!"
```

Expected output:

```
SUCESSO: senha redefinida para jsilva
TICKET: AD-jsilva-20261016-120000
```

### Com o Python (CLI)

```
uv run reset-senha-ad jsilva "N0vaSenha123!" --resolved-by suporte-ti
```

Ou instale o pacote no ambiente local:

```
pip install -e .
reset-senha-ad jsilva "N0vaSenha123!"
```

## Como rodar os testes / How to run tests

```
python -m ruff check . && python -m pytest -q
```

Resultado esperado: `8 passed`.

## Estrutura do projeto / Project structure

```
reset-senha-ad-automacao/
├── BRIEF.md
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   ├── Reset-SenhaAD.ps1     # script PowerShell: reset de senha no AD + ticket
│   └── reset_senha_ad/
│       ├── __init__.py
│       ├── ad_client.py      # protocolo AdClient e implementacao PowerShell
│       ├── cli.py            # linha de comando
│       ├── models.py         # Ticket e ResetResult
│       ├── orchestrator.py   # reset + ticket
│       └── ticket.py         # geracao de tickets sequenciais
└── tests/
    ├── conftest.py
    ├── test_ad_client.py
    ├── test_orchestrator.py
    └── test_ticket.py
```

## Licenca / License

MIT License. Veja o arquivo `LICENSE`.

Autor / Author: Kelvin Oliveira.
