from .model_tests import run_model_tests
from .service_tests import run_service_tests
from .util_tests import run_util_tests

separator_length: int = 124
finished_total: int = 0
finished_success: int = 0


def calculate_result(result):
    global finished_total, finished_success
    finished_total += result[0]
    finished_success += result[1]


def test_services():
    print("Starting service-tests...\n")
    calculate_result(run_service_tests())
    print("\nService-tests finished.")
    print("=" * separator_length)


def test_models():
    print("Starting model-tests...\n")
    calculate_result(run_model_tests())
    print("\nModel-tests finished.")
    print("=" * separator_length)


def test_utils():
    print("Starting util-tests...\n")
    calculate_result(run_util_tests())
    print("\nUtil-tests finished.")
    print("=" * separator_length)


def run_tests():
    print("=" * separator_length)
    print("Starting all tests...")
    print("=" * separator_length)

    test_services()
    test_models()
    test_utils()

    print("All tests finished.")
    print(f"Result: {finished_success}/{finished_total} successful")
    print("=" * separator_length)


if __name__ == "__main__":
    run_tests()
