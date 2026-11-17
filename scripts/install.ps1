# Thin launcher; all logic lives in install.py.
$ErrorActionPreference = 'Stop'
$py = $null
foreach ($name in @('python3', 'python', 'py')) {
  $cmd = Get-Command $name -ErrorAction SilentlyContinue
  if (-not $cmd) { continue }
  $prev = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  $out = $null
  try { $out = & $cmd.Source --version 2>&1 } finally { $ErrorActionPreference = $prev }
  if ($LASTEXITCODE -eq 0 -and "$out" -match 'Python') { $py = $cmd; break }
}
if (-not $py) { throw 'no working Python (python3 / python / py); install from python.org' }
& $py.Source (Join-Path $PSScriptRoot 'install.py') @args
exit $LASTEXITCODE
