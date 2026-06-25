import customtkinter as ctk
from settings import load_config
from obs_controller import OBSController, OBSConfig
from fm_controller import launch_fm25
from commentary import goal_commentary

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FM25AIStudio(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FM25 AI Studio v0.1")
        self.geometry("720x520")

        self.config_data = load_config()
        obs_cfg = self.config_data["obs"]
        self.obs = OBSController(OBSConfig(obs_cfg["host"], obs_cfg["port"], obs_cfg["password"]))

        self.status = ctk.CTkTextbox(self, height=120)
        self.status.pack(padx=20, pady=20, fill="x")
        self.log("FM25 AI Studio ready.")

        grid = ctk.CTkFrame(self)
        grid.pack(padx=20, pady=10, fill="both", expand=True)

        buttons = [
            ("Connect OBS", self.connect_obs),
            ("Launch FM25", self.launch_fm),
            ("Starting Soon", lambda: self.scene("Starting Soon")),
            ("Pre-Match", lambda: self.scene("Pre-Match")),
            ("Live Match", lambda: self.scene("Live Match")),
            ("Half-Time", lambda: self.scene("Half-Time")),
            ("Full-Time", lambda: self.scene("Full-Time")),
            ("Stream Ending", lambda: self.scene("Stream Ending")),
            ("Test Scoreboard", self.test_scoreboard),
            ("Test Goal Commentary", self.test_goal),
        ]

        for i, (label, cmd) in enumerate(buttons):
            btn = ctk.CTkButton(grid, text=label, command=cmd, height=42)
            btn.grid(row=i//2, column=i%2, padx=12, pady=12, sticky="ew")
        grid.grid_columnconfigure((0,1), weight=1)

    def log(self, msg: str):
        self.status.insert("end", msg + "\n")
        self.status.see("end")

    def connect_obs(self):
        try:
            self.log(self.obs.connect())
        except Exception as e:
            self.log(f"OBS connection failed: {e}")

    def launch_fm(self):
        self.log(launch_fm25(self.config_data["fm25"]["exe_path"]))

    def scene(self, name: str):
        try:
            self.obs.set_scene(name)
            self.log(f"Scene switched: {name}")
        except Exception as e:
            self.log(f"Scene switch failed: {e}")

    def test_scoreboard(self):
        b = self.config_data["broadcast"]
        try:
            self.obs.update_scoreboard(b["home_team"], b["away_team"], 2, 1, "74:23")
            self.log("Scoreboard test sent to OBS.")
        except Exception as e:
            self.log(f"Scoreboard update failed: {e}")

    def test_goal(self):
        try:
            text = goal_commentary("HOME", "74'")
            self.obs.commentary(text)
            self.log("Goal commentary test sent to OBS.")
        except Exception as e:
            self.log(f"Commentary update failed: {e}")

if __name__ == "__main__":
    app = FM25AIStudio()
    app.mainloop()
