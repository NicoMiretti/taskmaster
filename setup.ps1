# TaskMaster v1.0 - Setup Script
# Run this script to set up the project for the first time

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "TaskMaster v1.0 - Setup" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Check if venv exists
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment found" -ForegroundColor Green
} else {
    Write-Host "✗ Virtual environment not found. Creating..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
if (Test-Path ".env") {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
} else {
    Write-Host "Creating .env file from .env.example..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "✓ .env file created. Please edit it with your settings" -ForegroundColor Green
}

Write-Host ""
Write-Host "Running database migrations..." -ForegroundColor Yellow
python manage.py migrate

Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Create a superuser: python manage.py createsuperuser" -ForegroundColor White
Write-Host "2. Run the server: python manage.py runserver" -ForegroundColor White
Write-Host "3. Open http://localhost:8000 in your browser" -ForegroundColor White
Write-Host ""
