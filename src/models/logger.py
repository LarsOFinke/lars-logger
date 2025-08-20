from __future__ import annotations

import time

from functools import wraps

from .logger_config import LoggerConfig
from ..services.path_service import PathService
from ..services.file_service import FileService


class Logger:
    path_service = PathService()
    file_service = FileService()

    def __init__(
        self, name: str = "Logger", config: LoggerConfig | None = None
    ) -> None:
        self.name = name
        self.config = LoggerConfig() if config is None else config
        self.file_path: str = self.path_service.get_log_file_path(
            self.config.log_file_name, self.config.log_file_type
        )

    def _check_log_level(self, level: str):
        if self.config.dev_mode:
            return True
        if level in self.config.log_level_includes[self.config.log_level]:
            return True
        return False

    def log(self, message: str, level="info"):
        if self._check_log_level(level):
            if self.config.log_console:
                print(f"({level}) | {message}")

            if self.config.log_file:
                match self.config.log_file_type:
                    case "text":
                        self.file_service.append_text_message_to_file(
                            file_path=self.file_path, level=level, message=message
                        )
                    case "json":
                        self.file_service.append_json_message_to_file(
                            file_path=self.file_path, level=level, message=message
                        )

    # Instance-decorator: @logger.log_duration
    def log_duration(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if not self.config.dev_mode:
                # PROD: run the function, no timing logs
                return func(*args, **kwargs)

            # DEV: log start + duration
            self.log(f"{func.__name__} started.", "duration")
            start = time.perf_counter()
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.log(str(e), "error")  # ensure string
                raise
            finally:
                elapsed = time.perf_counter() - start
                self.log(f"{func.__name__} took {elapsed*1000:.2f} ms", "duration")

        return wrapped

    def __repr__(self):
        return (
            f"Logger-Name: {self.name} | "
            f"File-Path: {self.file_path} | "
            f"Config -> {self.config} | "
            f"Path-Service -> {self.path_service} | "
            f"File-Service -> {self.file_service}"
        )
