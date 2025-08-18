from __future__ import annotations

from .logger_config import LoggerConfig
from ..services.path_service import PathService
from ..services.file_service import FileService


class Logger:
    path_service = PathService()
    file_service = FileService()

    def __init__(self, name: str = "", config: LoggerConfig | None = None) -> None:
        self.name = name
        self.config = LoggerConfig() if config is None else config
        self.file_path: str = self.path_service.get_log_file_path(self.config.file_name)

    def __repr__(self):
        return (
            f"Name: {self.name} | \n"
            f"File-Path: {self.file_path} | \n"
            f"Config -> {self.config} | \n"
            f"Path-Service -> {self.path_service}"
        )

    def log(self, message: str, level="info"):
        if self.config.console_output:
            print(f"({level}) | {message}")

        if self.config.file_output:
            self.file_service.append_message_to_file(self.file_path, message, level)
