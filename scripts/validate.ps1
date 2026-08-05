$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
python -c "import yaml,sys; sys.exit(0 if yaml.__version__ == '6.0.3' else 1)"; if ($LASTEXITCODE -ne 0) { throw "Install exact requirements-validation.txt dependency versions" }
Write-Host "WORKING: semantic repository and whitespace validation"
python tools/validate_repo.py; if ($LASTEXITCODE -ne 0) { throw "Repository validation failed" }
Write-Host "WORKING: staged Git whitespace equivalence"
python tools/check_staged_whitespace.py; if ($LASTEXITCODE -ne 0) { throw "Staged Git whitespace check failed" }
Write-Host "WORKING: public-boundary scan"
python tools/scan_public_boundary.py; if ($LASTEXITCODE -ne 0) { throw "Public-boundary scan failed" }
Write-Host "WORKING: positive and mutation tests"
python -m unittest discover -s tests -v; if ($LASTEXITCODE -ne 0) { throw "Tests failed" }
Write-Host "WORKING: manifest and checksum verification"
python tools/generate_manifest.py --check; if ($LASTEXITCODE -ne 0) { throw "Manifest verification failed" }
$Temp = Join-Path ([System.IO.Path]::GetTempPath()) ("qrsc-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $Temp | Out-Null
try {
  python tools/build_release.py --output (Join-Path $Temp "a.zip") | Out-Null
  python tools/build_release.py --output (Join-Path $Temp "b.zip") | Out-Null
  $A=(Get-FileHash (Join-Path $Temp "a.zip") -Algorithm SHA256).Hash
  $B=(Get-FileHash (Join-Path $Temp "b.zip") -Algorithm SHA256).Hash
  if ($A -ne $B) { throw "Deterministic build mismatch" }
} finally { Remove-Item -Recurse -Force $Temp }
if ($env:VALIDATE_NETWORK -eq "1") {
  python tools/check_external_links.py; if ($LASTEXITCODE -ne 0) { throw "External-link validation failed" }
}
Write-Host "PASS: complete documentation-first release validation"
