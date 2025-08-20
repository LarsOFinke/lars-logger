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

    def log(self, message: str, level="info"):
        if self.config.dev_mode or level in self.config.log_level_includes[level]:
            if self.config.log_console:
                print(f"({level}) | {message}")

            if self.config.log_file and self.config.log_file_type == "text":
                self.file_service.append_text_message_to_file(
                    file_path=self.file_path, level=level, message=message
                )
            elif self.config.log_file and self.config.log_file_type == "json":
                self.file_service.append_json_message_to_file(
                    file_path=self.file_path, level=level, message=message
                )

    # Instance-decorator: @logger.log_duration
    def log_duration(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if self.config.dev_mode:
                self.log(f"LOG-DURATION START | {func.__name__} started.")
                start = time.perf_counter()
                try:
                    return func(*args, **kwargs)  # just run it
                except Exception as e:
                    self.log(e, "error")
                finally:
                    elapsed = time.perf_counter() - start
                    self.log(
                        f"LOG-DURATION END | {func.__name__} took {elapsed*1000:.2f} ms"
                    )

        return wrapped

    def __repr__(self):
        return (
            f"Logger-Name: {self.name} | \n"
            f"File-Path: {self.file_path} | \n"
            f"Config -> {self.config} | \n"
            f"Path-Service -> {self.path_service} | \n"
            f"File-Service -> {self.file_service}"
        )
