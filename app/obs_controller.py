from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

try:
    from obsws_python import ReqClient
except ImportError:  # Allows UI to open before requirements are installed
    ReqClient = None


@dataclass
class OBSConfig:
    host: str
    port: int
    password: str


class OBSController:
    def __init__(self, config: OBSConfig):
        self.config = config
        self.client: Optional[ReqClient] = None

    def connect(self) -> str:
        if ReqClient is None:
            return "obsws-python is not installed. Run: pip install -r requirements.txt"
        self.client = ReqClient(
            host=self.config.host,
            port=self.config.port,
            password=self.config.password,
            timeout=3,
        )
        version = self.client.get_version()
        return f"Connected to OBS WebSocket: {version.obs_version}"

    def set_scene(self, scene_name: str) -> None:
        self._require_client()
        self.client.set_current_program_scene(scene_name)

    def set_text(self, source_name: str, text: str) -> None:
        self._require_client()
        self.client.set_input_settings(source_name, {"text": text}, True)

    def update_scoreboard(self, home: str, away: str, hs: int, as_: int, clock: str) -> None:
        self.set_text("Scoreboard Text", f"{home}   {hs} - {as_}   {away}")
        self.set_text("Clock Text", clock)

    def commentary(self, text: str) -> None:
        self.set_text("Commentary Text", text)

    def _require_client(self) -> None:
        if self.client is None:
            raise RuntimeError("OBS is not connected")
