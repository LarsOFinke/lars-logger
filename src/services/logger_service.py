from ..models.logger import Logger, LoggerConfig


class LoggerService:

    def __init__(self):
        pass

    def get_logger_config(
        self,
        dev_mode: bool,
        log_level: str,
        log_console: bool,
        log_file: bool,
        log_file_name: str,
        log_file_type: str,
    ):
        return LoggerConfig(
            dev_mode=dev_mode,
            log_level=log_level,
            log_console=log_console,
            log_file=log_file,
            log_file_name=log_file_name,
            log_file_type=log_file_type,
        )

    def get_default_logger(self, name="Logger"):
        return Logger(name=name)

    def get_custom_logger(self, name, config):
        return Logger(name=name, config=config)

    def get_json_logger(self, name="Logger"):
        test_cfg = LoggerConfig(
            dev_mode=False,
            log_console=False,
            log_file=True,
            log_file_name="log",
            log_file_type="json",
        )
        return Logger(name=name, config=test_cfg)

    def get_dev_logger(self):
        dev_cfg = LoggerConfig(
            dev_mode=True,
            log_console=True,
            log_file=True,
            log_file_name="dev-log",
            log_file_type="text",
        )
        return Logger(name="Dev-Logger", config=dev_cfg)

    def get_test_logger(self):
        dev_cfg = LoggerConfig(
            dev_mode=True,
            log_console=True,
            log_file=True,
            log_file_name="test-log",
            log_file_type="text",
        )
        return Logger(name="Test-Logger", config=dev_cfg)
