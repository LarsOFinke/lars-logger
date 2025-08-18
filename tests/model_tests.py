from src.models.logger_config import LoggerConfig
from src.models.logger import Logger


def test_logger_model():
    try:
        print("Starting logger-model-tests...")
        logger = Logger()
        print(f"Logger - {logger}")
        test_logger_functionality(logger, visible=False)
        print("Logger-model-Tests erfolgreich beendet.")
    except Exception as e:
        print(e)


def test_logger_functionality(logger: Logger, visible=True):
    try:
        print("Starting logger-functionality-tests...")
        logger.info(f"Info-Test - {"SICHTBAR" if visible else "NICHT SICHTBAR"}")
        print("Logger-functionality-Tests erfolgreich beendet.")
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
        test_logger_functionality(custom_logger)
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
