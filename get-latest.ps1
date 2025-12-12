# get-latest.ps1 - Pull latest changes from hta-schema-tools repository

Write-Host "=== HTA Schema Tools: Get Latest ===" -ForegroundColor Cyan

# Check if we're in a git repository
if (-not (Test-Path .git)) {
    Write-Host "ERROR: Not a git repository. Run this from hta-schema-tools directory." -ForegroundColor Red
    exit 1
}

# Check for uncommitted changes
$status = git status --porcelain
if ($status) {
    Write-Host "WARNING: You have uncommitted changes:" -ForegroundColor Yellow
    git status --short
    Write-Host ""
    $response = Read-Host "Stash changes before pulling? (y/n)"
    if ($response -eq 'y') {
        git stash save "Auto-stash before pull $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        Write-Host "Changes stashed." -ForegroundColor Green
    }
}

# Pull latest changes
Write-Host "Pulling latest changes from origin/main..." -ForegroundColor Cyan
git pull origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Successfully pulled latest changes" -ForegroundColor Green
    
    # Show latest commit
    Write-Host ""
    Write-Host "Latest commit:" -ForegroundColor Cyan
    git log -1 --oneline
} else {
    Write-Host "✗ Failed to pull changes" -ForegroundColor Red
    exit 1
}

# If we stashed, remind user
$stashList = git stash list
if ($stashList) {
    Write-Host ""
    Write-Host "You have stashed changes. Run 'git stash pop' to restore them." -ForegroundColor Yellow
}
