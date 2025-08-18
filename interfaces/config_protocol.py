from typing import TypedDict, Literal


class ConfigProtocol(TypedDict):
    dev_mode: bool
    console_output: bool
    file_output: bool
    file_type: Literal["json", "txt", "csv"]
