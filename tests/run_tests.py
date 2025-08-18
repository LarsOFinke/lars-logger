from model_tests import run_model_tests
from service_tests import run_service_tests
from util_tests import run_util_tests


def run_tests():
    print("Starting all tests...")

    print("Starting model-tests...")
    run_model_tests()

    print("Starting service-tests...")
    run_service_tests()

    print("Starting util-tests...")
    run_util_tests()


if __name__ == "__main__":
    run_tests()
