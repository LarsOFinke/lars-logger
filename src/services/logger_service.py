from ..models.logger import Logger, LoggerConfig


class LoggerService:

    def __init__(self):
        pass

    def get_logger(self, name=""):
        return Logger(name=name)

    def get_json_logger(self, name=""):
        test_cfg = LoggerConfig(
            dev_mode=False,
            console_output=False,
            file_output=True,
            file_type="json",
        )
        return Logger(name=name, config=test_cfg)

    def get_dev_logger(self, name=""):
        dev_cfg = LoggerConfig(
            dev_mode=True,
            console_output=True,
            file_output=True,
            file_type="text",
        )
        return Logger(name=name, config=dev_cfg)
