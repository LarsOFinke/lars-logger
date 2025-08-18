from src.models.logger import Logger
from src.models.logger_config import LoggerConfig


def test_logger_model():
    try:
        print("Starting logger-model-tests...")
        logger = Logger()
        print(f"Logger: {logger}")
    except Exception as e:
        print(e)


def test_logger_config_model():
    try:
        print("Starting logger-config-tests...")
        logger_config = LoggerConfig()
        print(f"Logger-Config: {logger_config}")
    except Exception as e:
        print(e)


def run_model_tests():
    try:
        test_logger_model()
        test_logger_config_model()
    except Exception as e:
        print(e)
