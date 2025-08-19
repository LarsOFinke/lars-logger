from ..models.logger import Logger, LoggerConfig


class LoggerService:

    def __init__(self):
        pass

    def create_test_logger(self, name=""):
        test_cfg = LoggerConfig(
            dev_mode=False,  # Default
            console_output=False,  # Default
            file_output=True,  # Default
            file_name="custom-log",  # Optional
            file_type="json",  # "text" / "json" / ...
        )
        return Logger(name=name, config=test_cfg)

    def create_dev_logger(self, name=""):
        dev_cfg = LoggerConfig(
            dev_mode=True,
            console_output=True,
            file_output=True,
            file_type="json",  # "text" / "json" / ...
        )
        return Logger(name=name, config=dev_cfg)
