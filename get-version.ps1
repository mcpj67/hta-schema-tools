# get-version.ps1 - View or checkout a previous version of hta-schema-tools

param(
    [Parameter(Mandatory=$false)]
    [string]$Version,
    
    [Parameter(Mandatory=$false)]
    [switch]$Checkout
)

Write-Host "=== HTA Schema Tools: Version History ===" -ForegroundColor Cyan

# Check if we're in a git repository
if (-not (Test-Path .git)) {
    Write-Host "ERROR: Not a git repository. Run this from hta-schema-tools directory." -ForegroundColor Red
    exit 1
}

# List all tags if no version specified
if (-not $Version) {
    Write-Host ""
    Write-Host "Available versions:" -ForegroundColor Cyan
    git tag -l --sort=-version:refname
    
    Write-Host ""
    Write-Host "Usage:" -ForegroundColor Yellow
    Write-Host "  .\get-version.ps1 v1.0.0              # View version details"
    Write-Host "  .\get-version.ps1 v1.0.0 -Checkout    # Checkout this version"
    Write-Host "  .\get-version.ps1                     # List all versions"
    exit 0
}

# Ensure version starts with 'v'
if (-not $Version.StartsWith('v')) {
    $Version = "v$Version"
}

# Check if tag exists
$existingTag = git tag -l $Version
if (-not $existingTag) {
    Write-Host "ERROR: Version $Version not found." -ForegroundColor Red
    Write-Host ""
    Write-Host "Available versions:" -ForegroundColor Cyan
    git tag -l
    exit 1
}

# Show version details
Write-Host ""
Write-Host "Version: $Version" -ForegroundColor Green
Write-Host ""
Write-Host "Tag message:" -ForegroundColor Cyan
git tag -l -n99 $Version
Write-Host ""
Write-Host "Commit details:" -ForegroundColor Cyan
git show $Version --stat

# Checkout if requested
if ($Checkout) {
    Write-Host ""
    $status = git status --porcelain
    if ($status) {
        Write-Host "WARNING: You have uncommitted changes." -ForegroundColor Yellow
        git status --short
        Write-Host ""
        $response = Read-Host "Stash changes before checkout? (y/n)"
        if ($response -eq 'y') {
            git stash save "Auto-stash before checkout $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
            Write-Host "Changes stashed." -ForegroundColor Green
        } else {
            Write-Host "Checkout cancelled." -ForegroundColor Yellow
            exit 1
        }
    }
    
    Write-Host ""
    Write-Host "Checking out version $Version..." -ForegroundColor Cyan
    git checkout $Version
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✓ Successfully checked out $Version" -ForegroundColor Green
        Write-Host ""
        Write-Host "WARNING: You are in 'detached HEAD' state." -ForegroundColor Yellow
        Write-Host "To return to main branch: git checkout main" -ForegroundColor Yellow
    } else {
        Write-Host "✗ Checkout failed" -ForegroundColor Red
        exit 1
    }
}
