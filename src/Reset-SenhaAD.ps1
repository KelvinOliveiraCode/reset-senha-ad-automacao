<#
.SYNOPSIS
    Redefine a senha de um usuario no Active Directory e reporta um ticket de suporte.
.DESCRIPTION
    Usa o modulo ActiveDirectory do PowerShell para redefinir a senha e o pacote
    Python reset-senha-ad-automacao para gerar o ticket de suporte associado.
.PARAMETER Username
    Login do usuario no AD (sAMAccountName).
.PARAMETER NewPassword
    Nova senha do usuario.
.PARAMETER ResolvedBy
    Quem executa o reset (padrao: suporte-ti).
.EXAMPLE
    .\Reset-SenhaAD.ps1 -Username jsilva -NewPassword "N0vaSenha123!"
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Username,

    [Parameter(Mandatory = $true)]
    [string]$NewPassword,

    [string]$ResolvedBy = "suporte-ti"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

try {
    $senhaSegura = ConvertTo-SecureString -String $NewPassword -AsPlainText -Force
    Set-ADAccountPassword -Identity $Username -NewPassword $senhaSegura -Reset | Out-Null
    Write-Output "SUCESSO: senha redefinida para $Username"
}
catch {
    Write-Error ("Falha ao redefinir a senha de {0}: {1}" -f $Username, $_.Exception.Message)
    exit 1
}

$data = Get-Date -Format "yyyyMMdd-HHmmss"
$ticketId = "AD-{0}-{1}" -f $Username, $data
Write-Output ("TICKET: {0}" -f $ticketId)
