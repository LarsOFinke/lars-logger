from __future__ import annotations

from .logger_config import LoggerConfig
from ..services.file_service import FileService


class Logger:
    file_service = FileService()

    def __init__(self, name: str = "", config: LoggerConfig | None = None) -> None:
        self.name = name
        self.config = LoggerConfig() if config is None else config
        self.file_path: str = self.file_service.get_log_file_path(self.config.file_name)

    def __repr__(self):
        return (
            f"Name: {self.name} | "
            "\n"
            f"Config -> {self.config} | "
            "\n"
            f"File-Service -> {self.file_service}"
        )
