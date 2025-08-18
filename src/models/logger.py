from __future__ import annotations

from .logger_config import LoggerConfig
from ..services.file_service import FileService


class Logger:
    def __init__(self, name: str = "", config: LoggerConfig | None = None) -> None:
        self.name = name
        self.config = LoggerConfig() if config is None else config
        self.file_service = FileService()
