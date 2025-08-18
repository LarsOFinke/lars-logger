from src.services.path_service import PathService


def test_path_service():
    try:
        print("Starting path-service-tests...")
        path_service = PathService()
        print(f"Path-Service - {path_service}")
        print(f"Log-File-Path: {path_service.get_log_file_path("test")}")
        print("Path-Service-Tests erfolgreich beendet.")
    except Exception as e:
        print(e)


def run_service_tests():
    try:
        test_path_service()
    except Exception as e:
        print(e)
