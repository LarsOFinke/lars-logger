from __future__ import annotations

from .logger_config import LoggerConfig
from ..services.logger_service import LoggerService


class Logger:
    def __init__(self, name: str, config: LoggerConfig | None = None) -> None:
        self.name = name
        self.config = LoggerConfig() if config is None else config
        self.service = LoggerService()
