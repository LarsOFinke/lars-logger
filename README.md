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

`Setup`

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

`Useage`

```python
from lars_logger.src.services.logger_service import LoggerService

DEV_MODE = True
JSON = False

logger_service = LoggerService()
# get_logger_config(dev_mode: bool, console_output: bool, file_output: bool, file_name: str, file_type: str,)
# get_custom_logger(self, name: str, config: LoggerConfig)
# get_test_logger()

if DEV_MODE:
    logger = logger_service.get_dev_logger()
elif JSON:
    logger = logger_service.get_json_logger()
else:
    logger = logger_service.get_default_logger()


logger.log(message="Its a log!", level="info")  # "info" (default) / "warning" / "error"


@logger.log_duration
def test():
    print("Testing log_duration-functionality")
```

`Tests`

```python
from src.services.logger_service import test_logger as logger

finished: int = 0
successful: int = 0


def finish_test(success=True):
    global finished, successful
    finished += 1
    successful += 1 if success else 0


def start_test(test: callable):
    if test():
        finish_test()
    else:
        finish_test(False)


def test_logging():
    try:
        print("Starting logging-tests...")
        print(logger)
        logger.log("Test-Log entry - Info")
        logger.log("Test-Log entry - Warning", "warning")
        logger.log("Test-Log entry - Error", "error")
        print("Logging-tests successful.")
        return True
    except Exception as e:
        print(e)
        return False


@logger.log_duration
def run_logger_tests():
    try:
        global finished, successful
        start_test(test_logging)
        return (finished, successful)
    except Exception as e:
        print(e)
```
