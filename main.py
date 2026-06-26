import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from app.core.obs_controller import OBSController

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class GripOnGamesStudio(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.obs = OBSController()

        self.title("GripOnGames Studio v0.4.0")
        self.geometry("1280x720")
        self.minsize(1100, 650)

        self.build_ui()
        self.add_log("GripOnGames Studio started.")
        self.add_log("Ready for OBS connection.")

    def build_ui(self):
        self.sidebar = ctk.CTkFrame(self, width=230)
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(
            self.sidebar,
            text="🎮 GripOnGames\nStudio",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=25)

        buttons = [
            ("Dashboard", None),
            ("Connect OBS", self.connect_obs),
            ("Start Stream", self.start_stream),
            ("Stop Stream", self.stop_stream),
            ("Start Recording", self.start_recording),
            ("Stop Recording", self.stop_recording),
        ]

        for text, command in buttons:
            ctk.CTkButton(
                self.sidebar,
                text=text,
                width=190,
                command=command
            ).pack(pady=7)

        self.main = ctk.CTkFrame(self)
        self.main.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            self.main,
            text="GripOnGames Studio",
            font=("Segoe UI", 34, "bold")
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            self.main,
            text="The Ultimate AI Broadcast Studio for Football Gaming",
            font=("Segoe UI", 16)
        ).pack(pady=(0, 20))

        self.status_frame = ctk.CTkFrame(self.main)
        self.status_frame.pack(fill="x", padx=20, pady=10)

        self.obs_status = self.status_card("OBS", "🔴 Disconnected")
        self.game_status = self.status_card("Game", "⚪ Not Running")
        self.stream_status = self.status_card("Stream", "⚪ Offline")
        self.record_status = self.status_card("Recording", "⚪ Stopped")

        self.control_frame = ctk.CTkFrame(self.main)
        self.control_frame.pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(
            self.control_frame,
            text="Selected Game",
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.game_selector = ctk.CTkOptionMenu(
            self.control_frame,
            values=["Football Manager 2025", "EA Sports FC26"]
        )
        self.game_selector.pack(anchor="w", padx=20, pady=(0, 15))

        self.log_box = ctk.CTkTextbox(self.main, height=190)
        self.log_box.pack(fill="both", expand=True, padx=20, pady=20)
        self.log_box.insert("end", "Live Log\n")
        self.log_box.insert("end", "-----------------------------\n")

    def status_card(self, title, value):
        frame = ctk.CTkFrame(self.status_frame)
        frame.pack(side="left", fill="both", expand=True, padx=8, pady=8)

        ctk.CTkLabel(
            frame,
            text=title,
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(10, 3))

        label = ctk.CTkLabel(
            frame,
            text=value,
            font=("Segoe UI", 15)
        )
        label.pack(pady=(0, 10))

        return label

    def add_log(self, message):
        now = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{now}] {message}\n")
        self.log_box.see("end")

    def connect_obs(self):
        success, message = self.obs.connect()

        if success:
            self.obs_status.configure(text="🟢 Connected")
            self.add_log(message)
            messagebox.showinfo("OBS Connected", message)
        else:
            self.obs_status.configure(text="🔴 Failed")
            self.add_log(f"OBS connection failed: {message}")
            messagebox.showerror("OBS Error", message)

    def start_stream(self):
        success, message = self.obs.start_stream()
        if success:
            self.stream_status.configure(text="🟢 Live")
        self.add_log(message)

    def stop_stream(self):
        success, message = self.obs.stop_stream()
        if success:
            self.stream_status.configure(text="⚪ Offline")
        self.add_log(message)

    def start_recording(self):
        success, message = self.obs.start_recording()
        if success:
            self.record_status.configure(text="🔴 Recording")
        self.add_log(message)

    def stop_recording(self):
        success, message = self.obs.stop_recording()
        if success:
            self.record_status.configure(text="⚪ Stopped")
        self.add_log(message)


if __name__ == "__main__":
    app = GripOnGamesStudio()
    app.mainloop()