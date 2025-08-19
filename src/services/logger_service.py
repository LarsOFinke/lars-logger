from ..models.logger import Logger, LoggerConfig


class LoggerService:

    def __init__(self):
        pass

    def get_logger_config(
        self,
        dev_mode: bool,
        console_output: bool,
        file_output: bool,
        file_name: str,
        file_type: str,
    ):
        return LoggerConfig(dev_mode, console_output, file_output, file_name, file_type)

    def get_default_logger(self, name="Logger"):
        return Logger(name=name)

    def get_custom_logger(self, name, config):
        return Logger(name=name, config=config)

    def get_json_logger(self, name="Logger"):
        test_cfg = LoggerConfig(
            dev_mode=False,
            console_output=False,
            file_output=True,
            file_type="json",
        )
        return Logger(name=name, config=test_cfg)

    def get_dev_logger(self):
        dev_cfg = LoggerConfig(
            dev_mode=True,
            console_output=True,
            file_output=True,
            file_type="text",
        )
        return Logger(name="Dev-Logger", config=dev_cfg)

    def get_test_logger(self):
        dev_cfg = LoggerConfig(
            dev_mode=True,
            console_output=True,
            file_output=True,
            file_name="test-log",
            file_type="text",
        )
        return Logger(name="Test-Logger", config=dev_cfg)
