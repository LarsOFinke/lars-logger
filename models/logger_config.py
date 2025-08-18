from ..interfaces import ConfigProtocol


class LoggerConfig:

    def __init__(
        self,
        dev_mode: bool = False,
        console_output: bool = False,
        file_output: bool = True,
        file_type: str = "text",
    ):
        self.dev_mode: bool = dev_mode
        self.console_output: bool = console_output
        self.file_output: bool = file_output
        self.file_type: str = file_type

    def load_config(self, config: ConfigProtocol) -> bool:
        try:
            self.dev_mode: bool = config.dev_mode
            self.console_output: bool = config.console_output
            self.file_output: bool = config.file_output
            self.file_type: str = config.file_type
            return True

        except:
            return False
