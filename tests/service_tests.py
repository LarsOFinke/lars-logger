from src.services.path_service import PathService

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


def test_path_service() -> tuple[int]:
    try:
        print("Starting path-service-tests...")
        path_service = PathService()
        print(f"Path-Service - {path_service}")
        print(f"Log-File-Path: {path_service.get_log_file_path("test")}")
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
