## Quickstart

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

## Set up .env ###

# Update pip
python.exe -m pip install --upgrade pip

# Dependencies
pip install -e .

# Test Commands
logger-all-tests     # Alle Funktionalitäten und Einheiten testen
```