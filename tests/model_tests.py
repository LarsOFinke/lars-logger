from src.models.logger_config import LoggerConfig
from src.models.logger import Logger

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


def test_logger_model():
    try:
        print("Starting logger-model-tests...")
        logger = Logger()
        print(f"Logger - {logger}")
        test_logger_functionality(logger, visible=False)
        print("Logger-model-Tests erfolgreich beendet.")
        return True
    except Exception as e:
        print(e)
        return False


def test_logger_functionality(logger: Logger, visible=True):
    try:
        print("Starting logger-functionality-tests...")
        logger.log(f"Info-Test - {"SICHTBAR" if visible else "NICHT SICHTBAR"}")
        print("Logger-functionality-Tests erfolgreich beendet.")
        return True
    except Exception as e:
        print(e)
        return False


def test_logger_config_model():
    try:
        print("Starting logger-config-model-tests...")
        logger_config = LoggerConfig()
        print(f"Logger-Config - {logger_config}")
        print("Logger-Config-model-Tests erfolgreich beendet.")
        return True
    except Exception as e:
        print(e)
        return False


def test_custom_config():
    try:
        print("Starting custom-config-tests...")
        logger_config = LoggerConfig(dev_mode=True, console_output=True)
        print(f"Custom-Config - {logger_config}")
        custom_logger = Logger(config=logger_config)
        print(f"Custom-Logger - {custom_logger}")
        test_logger_functionality(custom_logger)
        print("Custom-config-Tests erfolgreich beendet.")
        return True
    except Exception as e:
        print(e)
        return False


def run_model_tests():
    try:
        global finished, successful
        start_test(test_logger_config_model)
        print()
        start_test(test_logger_model)
        print()
        start_test(test_custom_config)
        return (finished, successful)
    except Exception as e:
        print(e)
