import json
from datetime import datetime, timezone


class FileService:

    def __init__(self):
        pass

    def append_text_message_to_file(self, file_path: str, message: str, level: str):
        with open(file_path, "a") as f:
            f.write(f"({level}) | {message}\n")

    def append_json_message_to_file(
        self, file_path: str, level: str, message: str, **extra
    ) -> None:
        record = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "level": level,
            "message": message,
            **extra,  # optional: weitere Felder
        }

        # NDJSON: eine JSON-Zeile pro Logeintrag
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    record, ensure_ascii=False, separators=(",", ":"), default=str
                )
            )
            f.write("\n")

    def __repr__(self):
        return "File-Service ist initialisert."
