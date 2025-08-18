from src.models.logger_config import LoggerConfig
from src.models.logger import Logger


def test_logger_model():
    try:
        print("Starting logger-model-tests...")
        logger = Logger()
        print(f"Logger - {logger}")
        print("Logger-model-Tests erfolgreich beendet.")
    except Exception as e:
        print(e)


def test_logger_config_model():
    try:
        print("Starting logger-config-model-tests...")
        logger_config = LoggerConfig()
        print(f"Logger-Config - {logger_config}")
        print("Logger-Config-model-Tests erfolgreich beendet.")
    except Exception as e:
        print(e)


def run_model_tests():
    try:
        test_logger_config_model()
        print()
        test_logger_model()
    except Exception as e:
        print(e)
