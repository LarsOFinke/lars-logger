from model_tests import run_model_tests
from service_tests import run_service_tests
from util_tests import run_util_tests

separator_length = 124


def run_tests():
    print("=" * separator_length)
    print("Starting all tests...")
    print("=" * separator_length)

    print("Starting service-tests...\n")
    run_service_tests()
    print("\nService-tests finished.")
    print("=" * separator_length)

    print("Starting model-tests...\n")
    run_model_tests()
    print("\nModel-tests finished.")
    print("=" * separator_length)

    print("Starting util-tests...\n")
    run_util_tests()
    print("\nUtil-tests finished.")
    print("=" * separator_length)

    print("All tests finished.")
    print("=" * separator_length)


if __name__ == "__main__":
    run_tests()
