class FileService:

    def __init__(self):
        pass

    def append_message_to_file(self, file_path: str, message: str, level: str):
        with open(file_path, "a") as f:
            f.write(f"({level}) | {message}\n")
