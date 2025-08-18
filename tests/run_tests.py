from model_tests import test_logger_model
from service_tests import test_file_service
from util_tests import test_get_entry_file


def run_model_tests():
    test_logger_model()


def run_service_tests():
    test_file_service()


def run_util_tests():
    test_get_entry_file()


def run_tests():
    run_model_tests()
    run_service_tests()
    run_util_tests()


if __name__ == "__main__":
    run_tests()