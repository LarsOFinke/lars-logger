from src.models.logger_config import LoggerConfig
from src.models.logger import Logger


def test_logger_model():
    try:
        print("Starting logger-model-tests...")
        logger = Logger()
        print(f"Logger - {logger}")
        logger.info("Info-Test - NICHT SICHTBAR")
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


def test_custom_config():
    try:
        print("Starting custom-config-tests...")
        logger_config = LoggerConfig(dev_mode=True, console_output=True)
        print(f"Custom-Config - {logger_config}")
        custom_logger = Logger(config=logger_config)
        print(f"Custom-Logger - {custom_logger}")
        custom_logger.info("Info-Test - SICHTBAR")
        print("Custom-config-Tests erfolgreich beendet.")
    except Exception as e:
        print(e)


def run_model_tests():
    try:
        test_logger_config_model()
        print()
        test_logger_model()
        print()
        test_custom_config()
    except Exception as e:
        print(e)
