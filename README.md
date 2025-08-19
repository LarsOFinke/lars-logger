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

```python
from logger import Logger, LoggerConfig

cfg = LoggerConfig(
    dev_mode=False,  # Default
    console_output=False,  # Default
    file_output=True,  # Default
    file_name="custom-log",  # Optional
    file_type="json",  # "text" / "json" / ...
)

logger = Logger(config=cfg)
logger.log(message="Its a log!", level="info")  # "info" / "warning" / "error"
```

```python
from lars_logger.src.services.logger_service import LoggerService

logger_service = LoggerService()
logger = logger_service.create_dev_logger() # create_test_logger()
logger.log(message="Its a log!", level="info")  # "info" / "warning" / "error"

```
