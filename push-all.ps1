# push-all.ps1 - Commit and push all changes to hta-schema repository

param(
    [Parameter(Mandatory=$false)]
    [string]$Message
)

Write-Host "=== HTA Schema: Push All Changes ===" -ForegroundColor Cyan

# Check if we're in a git repository
if (-not (Test-Path .git)) {
    Write-Host "ERROR: Not a git repository. Run this from hta-schema directory." -ForegroundColor Red
    exit 1
}

# Check for changes
$status = git status --porcelain
if (-not $status) {
    Write-Host "No changes to commit." -ForegroundColor Yellow
    exit 0
}

# Show what will be committed
Write-Host ""
Write-Host "Changes to be committed:" -ForegroundColor Cyan
git status --short

# Get commit message if not provided
if (-not $Message) {
    Write-Host ""
    $Message = Read-Host "Enter commit message"
    if (-not $Message) {
        Write-Host "ERROR: Commit message required." -ForegroundColor Red
        exit 1
    }
}

# Add all changes
Write-Host ""
Write-Host "Staging all changes..." -ForegroundColor Cyan
git add .

# Commit
Write-Host "Committing changes..." -ForegroundColor Cyan
git commit -m $Message

if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Commit failed" -ForegroundColor Red
    exit 1
}

# Push to remote
Write-Host "Pushing to origin/main..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✓ Successfully pushed all changes" -ForegroundColor Green
    Write-Host ""
    Write-Host "Latest commit:" -ForegroundColor Cyan
    git log -1 --oneline
} else {
    Write-Host "✗ Push failed" -ForegroundColor Red
    Write-Host "Your changes are committed locally but not pushed." -ForegroundColor Yellow
    exit 1
}