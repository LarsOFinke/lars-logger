from src.services.file_service import FileService


def test_file_service():
    try:
        print("Starting file-service-tests...")
        file_service = FileService()
        print(f"File-Service - {file_service}")
        print("File-Service-Tests erfolgreich beendet.")
    except Exception as e:
        print(e)


def run_service_tests():
    try:
        test_file_service()
    except Exception as e:
        print(e)
