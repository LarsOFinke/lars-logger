class LoggerConfig:

    def __init__(
        self,
        dev_mode: bool = False,
        console_output: bool = False,
        file_output: bool = True,
        file_name: str = "log",
        file_type: str = "text",  # "text" / "json" / ...
    ):
        self.dev_mode: bool = dev_mode
        self.console_output: bool = console_output
        self.file_output: bool = file_output
        self.file_name: str = file_name
        self.file_type: str = file_type

    def __repr__(self):
        return (
            f"Dev-Mode: {self.dev_mode} | "
            f"Console-Output: {self.console_output} | "
            f"File-Output: {self.file_output} | "
            f"File-Name: {self.file_name} | "
            f"File-Type: {self.file_type}"
        )
