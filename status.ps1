# status.ps1 - Show repository status and recent history

param(
    [Parameter(Mandatory=$false)]
    [int]$Commits = 10
)

Write-Host "=== HTA Schema Tools: Repository Status ===" -ForegroundColor Cyan

# Check if we're in a git repository
if (-not (Test-Path .git)) {
    Write-Host "ERROR: Not a git repository. Run this from hta-schema-tools directory." -ForegroundColor Red
    exit 1
}

# Current branch
Write-Host ""
Write-Host "Current branch:" -ForegroundColor Cyan
git branch --show-current

# Remote info
Write-Host ""
Write-Host "Remote repository:" -ForegroundColor Cyan
git remote -v | Select-Object -First 1

# Uncommitted changes
Write-Host ""
Write-Host "Working directory status:" -ForegroundColor Cyan
$status = git status --porcelain
if ($status) {
    git status --short
} else {
    Write-Host "  Clean (no changes)" -ForegroundColor Green
}

# Unpushed commits
Write-Host ""
Write-Host "Unpushed commits:" -ForegroundColor Cyan
$unpushed = git log origin/main..HEAD --oneline 2>$null
if ($unpushed) {
    $unpushed
} else {
    Write-Host "  None (up to date with remote)" -ForegroundColor Green
}

# Recent commit history
Write-Host ""
Write-Host "Recent commits (last $Commits):" -ForegroundColor Cyan
git log --oneline --graph --decorate -n $Commits

# Tags
Write-Host ""
Write-Host "Recent tags:" -ForegroundColor Cyan
$tags = git tag -l --sort=-version:refname | Select-Object -First 5
if ($tags) {
    $tags
} else {
    Write-Host "  No tags yet" -ForegroundColor Yellow
}

# Summary
Write-Host ""
Write-Host "=== Quick Commands ===" -ForegroundColor Cyan
Write-Host "Get latest:      .\get-latest.ps1"
Write-Host "Push changes:    .\push-all.ps1 'commit message'"
Write-Host "Create version:  .\create-version.ps1 v1.1.0"
Write-Host "View versions:   .\get-version.ps1"
