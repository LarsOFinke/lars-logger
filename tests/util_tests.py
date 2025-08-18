from src.utils.file_helpers import get_entry_file, get_log_file_path


def test_get_entry_file():
    try:
        print("Starting get-entry-file-tests...")
        entry_file = get_entry_file()
        print(f"Entry-File: {entry_file}")
    except Exception as e:
        print(e)


def test_get_log_file_path():
    try:
        print("Starting get-log-file-path-tests...")
        log_file_path = get_log_file_path("test")
        print(f"Log-File-Path: {log_file_path}")
    except Exception as e:
        print(e)


def run_util_tests():
    try:
        test_get_entry_file()
        test_get_log_file_path()
    except Exception as e:
        print(e)
