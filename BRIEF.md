# BRIEF — reset-senha-ad-automacao

Projeto: automação de reset de senha AD (área Suporte TI).
Destino: C:\Users\Kelvin\AppData\Local\Temp\opencode\github-staging\projects\reset-senha-ad-automacao\
Validador (owner): workflow manager.

## Escopo (MVP)
- Reset de senha de usuário no Active Directory (PowerShell, módulo ActiveDirectory).
- Geração de ticket de suporte (sequencial, determinístico) em Python.
- Stack: PowerShell + Python, sem dependências externas.

## Entregas (arquivos criados)

Código:
- src/Reset-SenhaAD.ps1 — reset de senha no AD + impressão do ticket.
- src/reset_senha_ad/__init__.py
- src/reset_senha_ad/ad_client.py — protocolo AdClient + implementação PowerShell.
- src/reset_senha_ad/cli.py — CLI Python.
- src/reset_senha_ad/models.py — Ticket e ResetResult.
- src/reset_senha_ad/orchestrator.py — orquestrador reset + ticket.
- src/reset_senha_ad/ticket.py — geração de tickets sequenciais.

Testes:
- tests/conftest.py — FakeAdClient e fixtures.
- tests/test_ad_client.py — cliente AD falso e contrato.
- tests/test_orchestrator.py — orquestrador (sucesso, falha do AD, campos vazios).
- tests/test_ticket.py — geração determinística de tickets.

Documentação/licença:
- README.md — bilíngue PT-BR + EN (título, descrição, como usar, testes, licença MIT, autor Kelvin Oliveira).
- LICENSE — MIT (Kelvin Oliveira).
- BRIEF.md — este arquivo.
- pyproject.toml — projeto, scripts, pytest e ruff.

## Como verificar

1. Acesse a pasta do projeto:
   ```
   cd C:\Users\Kelvin\AppData\Local\Temp\opencode\github-staging\projects\reset-senha-ad-automacao
   ```

2. Rode o gate de verificação:
   ```
   python -m ruff check . && python -m pytest -q
   ```

3. Resultado esperado:
   - `All checks passed!` (ruff)
   - `8 passed in 0.0x s` (pytest)

4. Caminhos dos documentos:
   - README: C:\Users\Kelvin\AppData\Local\Temp\opencode\github-staging\projects\reset-senha-ad-automacao\README.md
   - BRIEF: C:\Users\Kelvin\AppData\Local\Temp\opencode\github-staging\projects\reset-senha-ad-automacao\BRIEF.md

## Critérios de aceitação (SPEC)

- [x] Reset funciona (via PowerShell Set-ADAccountPassword; Python orquestra com fake injetável para teste).
- [x] Testes que passem (8 passed, 0 falhados).
- [x] README PT/EN completo (título, descrição, como usar, testes, licença MIT, autor Kelvin Oliveira).

## Observação de design (não é bug)

O cliente AD real (PowerShellAdClient) não pode ser executado aqui sem um controlador de domínio; o contrato `AdClient` permite substituição por fake, que é o que os testes exercitam.
