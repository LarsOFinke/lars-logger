from src.services.logger_service import LoggerService, LoggerConfig
from src.services.path_service import PathService

from .model_tests import test_logger_functionality

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


def test_logger_service():
    try:
        print("Starting logger-service-tests...")
        logger_service = LoggerService()
        default_logger = logger_service.get_default_logger()
        print(default_logger)
        if not test_logger_functionality(default_logger, visible=False):
            return False

        custom_config = LoggerConfig(
            dev_mode=True,
            log_level="info",
            log_console=True,
            log_file=False,
            log_file_name="should-not-appear",
        )
        custom_logger = logger_service.get_custom_logger(
            "Test-Custom-Logger", custom_config
        )
        print(custom_logger)
        if not test_logger_functionality(custom_logger):
            return False

        dev_logger = logger_service.get_dev_logger()
        print(dev_logger)
        test_logger = logger_service.get_test_logger()
        print(test_logger)
        if not test_logger_functionality(test_logger):
            return False
        print("Logger-Service-Tests erfolgreich beendet.")
        return True
    except Exception as e:
        print(e)
        return False


def test_path_service():
    try:
        print("Starting path-service-tests...")
        path_service = PathService()
        print(f"Path-Service - {path_service}")
        print(f"Log-File-Path: {path_service.get_log_file_path("test", "json")}")
        print("Path-Service-Tests erfolgreich beendet.")
        return True
    except Exception as e:
        print(e)
        return False


def run_service_tests():
    try:
        global finished, successful
        start_test(test_path_service)
        return (finished, successful)
    except Exception as e:
        print(e)
