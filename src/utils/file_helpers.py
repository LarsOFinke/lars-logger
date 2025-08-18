import os
import sys


def get_entry_file() -> str:
    """Pfad der ausgeführten Startdatei (Script/Module/EXE) als String."""
    # PyInstaller/„frozen“: die EXE ist der Entry-Point
    if getattr(sys, "frozen", False):
        return os.path.realpath(sys.executable)

    # Normale Skripte oder `python -m paket.modul`
    m = sys.modules.get("__main__")
    if m is not None and getattr(m, "__file__", None):
        return os.path.realpath(m.__file__)  # -> e.g. /path/to/script.py

    # Fallback (manche Launcher/Wrapper)
    if sys.argv and sys.argv[0]:
        return os.path.realpath(sys.argv[0])

    # Letzter Ausweg (REPL/Jupyter): kein echtes Startfile -> Arbeitsverzeichnis
    return os.path.realpath(os.getcwd())


def get_log_file_path(file_name: str):
    entry_file = get_entry_file()
    entry_dir = os.path.dirname(entry_file)
    log_dir = os.path.join(entry_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, f"{file_name}.log")
    return log_file_path
