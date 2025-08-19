class LoggerConfig:

    def __init__(
        self,
        dev_mode: bool = False,
        log_level: str = "error",  # "info" / "warning" / "error"
        log_console: bool = False,
        log_file: bool = True,
        log_file_name: str = "prod-log",
        log_file_type: str = "text",  # "text" / "json" / ...
    ):
        self.dev_mode: bool = dev_mode
        self.log_level: str = log_level
        self.log_console: bool = log_console
        self.log_file: bool = log_file
        self.log_file_name: str = log_file_name
        self.log_file_type: str = log_file_type

    def __repr__(self):
        return (
            f"Dev-Mode: {self.dev_mode} | "
            f"Log-Level: {self.log_level} | "
            f"Log-Console-Output: {self.log_console} | "
            f"Log-File-Output: {self.log_file} | "
            f"Log-File-Name: {self.log_file_name} | "
            f"Log-File-Type: {self.log_file_type}"
        )
