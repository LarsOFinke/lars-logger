import os
import sys


class PathService:
    def __init__(self):
        self.entry_file = self.get_entry_file()
        self.entry_dir = os.path.dirname(self.entry_file)

    def get_entry_file(self) -> str:
        """Pfad der ausgeführten Startdatei (Script/Module/EXE) als String."""
        if getattr(sys, "frozen", False):
            return os.path.realpath(sys.executable)

        m = sys.modules.get("__main__")
        if m is not None and getattr(m, "__file__", None):
            return os.path.realpath(m.__file__)

        if sys.argv and sys.argv[0]:
            return os.path.realpath(sys.argv[0])

        return os.path.realpath(os.getcwd())

    # --- Helpers -------------------------------------------------------------

    def _find_project_root(self, start: str) -> str | None:
        """Suche nach Repo-/Projekt-Wurzel anhand von Markern."""
        cur = os.path.realpath(start)
        markers = ("pyproject.toml", ".git", "setup.cfg")
        while True:
            if any(os.path.exists(os.path.join(cur, m)) for m in markers):
                return cur
            parent = os.path.dirname(cur)
            if parent == cur:
                return None
            cur = parent

    def _prefer_base_dir(self) -> str:
        # 1) Expliziter Override
        env_dir = os.getenv("LOG_DIR")
        if env_dir:
            return os.path.realpath(env_dir)

        # 2) Unter pytest: CWD bzw. Projekt-Root vom CWD
        if "PYTEST_CURRENT_TEST" in os.environ:
            return self._find_project_root(os.getcwd()) or os.path.realpath(os.getcwd())

        # 3) Wenn Entry unter venv/Scripts|bin liegt: nimm CWD (typ. Projektordner)
        scripts_like = os.path.basename(self.entry_dir).lower() in {"scripts", "bin"}
        if scripts_like:
            venv_root = os.path.dirname(self.entry_dir)
            if os.path.exists(os.path.join(venv_root, "pyvenv.cfg")):
                return self._find_project_root(os.getcwd()) or os.path.realpath(
                    os.getcwd()
                )

        # 4) Versuche Projekt-Root vom Entry, sonst Entry-Dir
        return self._find_project_root(self.entry_dir) or self.entry_dir

    # --- Public API ----------------------------------------------------------

    def get_log_file_path(self, file_name: str) -> str:
        base = self._prefer_base_dir()
        log_dir = os.path.join(base, "logs")
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, f"{file_name}.log")

    def __repr__(self):
        return f"Entry-File: {self.entry_file} | Entry-Dir: {self.entry_dir}"
