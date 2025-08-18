from src.models.logger import Logger


def test_logger_model():
    try:
        print("Starting logger-model-tests...")
        logger = Logger()
        print(f"Logger: {logger}")
    except Exception as e:
        print(e)


def run_model_tests():
    try:
        test_logger_model()
    except Exception as e:
        print(e)
