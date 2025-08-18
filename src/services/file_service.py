import os
import sys


class FileService:

    def __init__(self):
        self.entry_file = self.get_entry_file()

    def get_entry_file(self) -> str:
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

    def get_log_file_path(self, file_name: str):
        entry_dir = os.path.dirname(self.entry_file)
        log_dir = os.path.join(entry_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, f"{file_name}.log")
        return log_file_path

    def __repr__(self):
        return f"Entry-File: {self.entry_file}"
