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


def test_dev_file_configs():
    try:
        print("Starting dev-file-config-tests...")

        print("Starting Dev-Console-Text-File-test.")
        dev_console_text_file_config = LoggerConfig(dev_mode=True, log_console=False)
        print(f"Dev-Console-Text-File-Config - {dev_console_text_file_config}")
        dev_console_text_file_logger = Logger(config=dev_console_text_file_config)
        print(f"Dev-Console-Text-File-Logger - {dev_console_text_file_logger}")
        test_logger_functionality(dev_console_text_file_logger)
        print("Dev-Console-Text-File-Config-Tests erfolgreich beendet.")

        print("Starting Dev-Console-Json-File-test.")
        dev_console_json_file_config = LoggerConfig(
            dev_mode=True, log_console=False, log_file_type="json"
        )
        print(f"Dev-Console-Json-File-Config - {dev_console_json_file_config}")
        dev_console_json_file_logger = Logger(config=dev_console_json_file_config)
        print(f"Dev-Console-Json-File-Logger - {dev_console_json_file_logger}")
        test_logger_functionality(dev_console_json_file_logger)
        print("Dev-Console-Json-File-Config-Tests erfolgreich beendet.")

        print("Dev-file-config-tests successful.")
        return True
    except Exception as e:
        print(e)
        return False


def test_custom_configs():
    try:
        print("Starting custom-config-tests...")
        test_dev_file_configs()
        print("Custom-config-tests successful.")
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
        start_test(test_custom_configs)
        return (finished, successful)
    except Exception as e:
        print(e)
