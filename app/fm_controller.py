import subprocess
from pathlib import Path


def launch_fm25(exe_path: str) -> str:
    path = Path(exe_path)
    if not path.exists():
        return f"FM25 not found at: {exe_path}"
    subprocess.Popen([str(path)], shell=False)
    return "Football Manager 25 launched"
