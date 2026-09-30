[CmdletBinding()]
param()

$ErrorActionPreference = 'Continue'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path

function Get-ToolStatus {
    param([string]$Name, [scriptblock]$Version)
    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $command) {
        return [pscustomobject]@{ Tool = $Name; Status = 'missing'; Detail = '' }
    }

    $detail = try { (& $Version 2>&1 | Select-Object -First 1) -join '' } catch { $_.Exception.Message }
    [pscustomobject]@{ Tool = $Name; Status = 'ok'; Detail = $detail }
}

$rows = @(
    Get-ToolStatus git { git --version }
    Get-ToolStatus gh { gh --version }
    Get-ToolStatus docker { docker --version }
    Get-ToolStatus python { python --version }
    Get-ToolStatus gcc { gcc --version }
    Get-ToolStatus clang { clang --version }
    Get-ToolStatus cl { cl 2>&1 }
    Get-ToolStatus cmake { cmake --version }
    Get-ToolStatus make { make --version }
    Get-ToolStatus ninja { ninja --version }
    Get-ToolStatus codex { codex --version }
    Get-ToolStatus wsl { wsl --status }
)

$rows | Format-Table -AutoSize

Write-Host "`nGitHub authentication:"
if (Get-Command gh -ErrorAction SilentlyContinue) { gh auth status 2>&1 }

Write-Host "`nDocker engine:"
if (Get-Command docker -ErrorAction SilentlyContinue) {
    docker info --format '{{.ServerVersion}}' 2>&1
} else {
    Write-Host 'unavailable (Docker CLI is not installed)'
}

Write-Host "`nRepository:"
git -C $repo status --short --branch 2>&1

Write-Host "`nWSL distributions:"
if (Get-Command wsl -ErrorAction SilentlyContinue) {
    wsl --list --verbose 2>&1
    Write-Host "`nWSL Ubuntu-24.04 toolchain:"
    foreach ($tool in @('gcc', 'g++', 'clang', 'make', 'cmake', 'ninja', 'gdb', 'python3', 'git')) {
        $output = & wsl -d Ubuntu-24.04 -- $tool --version 2>&1
        $code = $LASTEXITCODE
        [pscustomobject]@{
            Tool = $tool
            Status = if ($code -eq 0) { 'ok' } else { 'missing' }
            Detail = $output | Select-Object -First 1
        }
    }
}
