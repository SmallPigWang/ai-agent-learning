<#
.SYNOPSIS
  Verify that the Anchored Standard preset took effect in a session.

.DESCRIPTION
  Decompress and parse the session JSONL, then check:
  1. First-request tool schema is exactly the Minimal pair [bash, str_replace_editor]
  2. First-request config.maxTokens value
  3. First-request system is the Minimal persona ("You are a helpful software engineer assistant.")
  4. No agent-instructions / skill-catalog auto-injection before the first request
  5. After promotion (header #2 onward) the tool catalog recovers to the full set

.PARAMETER JsonlPath
  Path to session.jsonl.zstd. When empty, auto-pick the most recently modified session.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\verify-anchored.ps1
  powershell -ExecutionPolicy Bypass -File .\verify-anchored.ps1 -JsonlPath "C:\...\session.jsonl.zstd"
#>
param(
    [string]$JsonlPath = ""
)

$ErrorActionPreference = 'Stop'

# ── 1. Locate the session file ────────────────────────────────────────────
if (-not $JsonlPath) {
    $sessionsRoot = Join-Path $env:USERPROFILE '.dsh\sessions'
    if (-not (Test-Path -LiteralPath $sessionsRoot)) {
        Write-Error "sessions dir not found: $sessionsRoot"; exit 1
    }
    $JsonlPath = Get-ChildItem -Path $sessionsRoot -Recurse -Filter 'session.jsonl.zstd' -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1 -ExpandProperty FullName
}
if (-not $JsonlPath -or -not (Test-Path -LiteralPath $JsonlPath)) {
    Write-Error "session file not found: $JsonlPath"; exit 1
}
Write-Output "Session file: $JsonlPath"
Write-Output ""

# ── 2. Decompress and parse ───────────────────────────────────────────────
$zstd = Get-Command zstd -ErrorAction SilentlyContinue
if (-not $zstd) {
    Write-Error "zstd command not found; cannot decompress the session file."; exit 1
}
$raw = zstd -dc $JsonlPath 2>$null
if (-not $raw) { Write-Error "decompression failed or file is empty."; exit 1 }

$headers  = @()
$injected = @()
$firstHeaderSeq = [long]::MaxValue

foreach ($line in $raw) {
    if ($line -match '"type":"request/header"') {
        try {
            $o = $line | ConvertFrom-Json
            $headers += $o
            if ($o.seq -lt $firstHeaderSeq) { $firstHeaderSeq = [long]$o.seq }
        } catch {}
    }
    elseif ($line -match '"source":\{"kind":"agent-instructions"' -or $line -match '"source":\{"kind":"skill-catalog"') {
        try {
            $o = $line | ConvertFrom-Json
            $injected += $o
        } catch {}
    }
}

if ($headers.Count -eq 0) {
    Write-Output "WARN: no request/header event found (the session may not have sent a model request yet)."
    Write-Output "      Send a message in the Anchored Standard session, then run this script again."
    exit 0
}

# ── 3. Overview of all headers ────────────────────────────────────────────
Write-Output "=== request/header overview ($($headers.Count) total) ==="
$i = 0
foreach ($h in $headers) {
    $i++
    $names = @($h.data.header.tools | ForEach-Object { $_.name })
    $mt = $h.data.header.config.maxTokens
    Write-Output ("  header #{0}  seq={1}  tools={2}  maxTokens={3}" -f $i, $h.seq, $names.Count, $mt)
    Write-Output ("             tools=[{0}]" -f ($names -join ', '))
}
Write-Output ""

# ── 4. Per-item checks ────────────────────────────────────────────────────
$first  = $headers[0]
$fNames = @($first.data.header.tools | ForEach-Object { $_.name })
$fMax   = $first.data.header.config.maxTokens
$fSys   = [string]$first.data.header.system

Write-Output "=== checks ==="

# 4.1 first-request tool schema
$isMinimalPair = ($fNames.Count -eq 2) -and ($fNames -contains 'bash') -and ($fNames -contains 'str_replace_editor')
$mark1 = if ($isMinimalPair) { 'PASS' } else { 'FAIL' }
Write-Output "[$mark1] first-request tools == Minimal pair (bash + str_replace_editor)"
Write-Output "       actual: [$($fNames -join ', ')]"

# 4.2 first-request maxTokens
Write-Output "[INFO] first-request config.maxTokens = $fMax"

# 4.3 first-request system persona
$minimalPersona = 'You are a helpful software engineer assistant.'
$isMinimalPersona = ($fSys.Trim() -eq $minimalPersona)
$mark3 = if ($isMinimalPersona) { 'PASS' } else { 'FAIL' }
Write-Output "[$mark3] first-request system == Minimal persona"
if (-not $isMinimalPersona) {
    $len = [Math]::Min(120, $fSys.Length)
    Write-Output "       actual system start: $($fSys.Substring(0, $len))"
}

# 4.4 no auto-injection before the first request
$preInject = @($injected | Where-Object { $_.seq -lt $firstHeaderSeq })
$mark4 = if ($preInject.Count -eq 0) { 'PASS' } else { 'FAIL' }
Write-Output "[$mark4] no agent-instructions / skill-catalog injection before first request"
if ($preInject.Count -gt 0) {
    Write-Output ("       found {0} injection(s) (seq: {1})" -f $preInject.Count, (($preInject | ForEach-Object { $_.seq }) -join ', '))
}

# 4.5 promotion: header #2 onward recovers full catalog
$mark5 = 'N/A'
if ($headers.Count -ge 2) {
    $secondNames = @($headers[1].data.header.tools | ForEach-Object { $_.name })
    $isPromoted = $secondNames.Count -gt 2
    $mark5 = if ($isPromoted) { 'PASS' } else { 'FAIL' }
    Write-Output "[$mark5] header #2 recovered full catalog (tools count = $($secondNames.Count) > 2)"
} else {
    Write-Output "[N/A ] only one header so far; run another turn to check promotion"
}

Write-Output ""
$failCount = @($mark1, $mark3, $mark4, $mark5) | Where-Object { $_ -eq 'FAIL' } | Measure-Object | Select-Object -ExpandProperty Count
if ($failCount -eq 0) {
    Write-Output "Result: all key checks PASS (two-phase Anchored Standard is active)"
} else {
    Write-Output "Result: $failCount check(s) FAIL - review the actual values above."
}
