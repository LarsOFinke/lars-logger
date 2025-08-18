from ..utils.file_helpers import get_log_file_path


class LoggerConfig:

    def __init__(
        self,
        dev_mode: bool = False,
        console_output: bool = False,
        file_output: bool = True,
        file_name: str = "log",
        file_type: str = "text",
    ):
        self.dev_mode: bool = dev_mode
        self.console_output: bool = console_output
        self.file_output: bool = file_output
        self.file_name: str = file_name
        self.file_type: str = file_type
        self.file_path: str = get_log_file_path(self.file_name)
