import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class FM25AIStudio(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("FM25 AI Studio v0.2")
        self.geometry("1280x720")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220)
        self.sidebar.pack(side="left", fill="y")

        title = ctk.CTkLabel(
            self.sidebar,
            text="FM25 AI Studio",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(pady=25)

        menu = [
            "Dashboard",
            "OBS",
            "Football Manager",
            "AI Commentary",
            "Statistics",
            "Settings"
        ]

        for item in menu:
            button = ctk.CTkButton(
                self.sidebar,
                text=item,
                width=180
            )
            button.pack(pady=8)

        # Main Area
        self.main = ctk.CTkFrame(self)
        self.main.pack(side="right", fill="both", expand=True)

        welcome = ctk.CTkLabel(
            self.main,
            text="Welcome to FM25 AI Studio",
            font=("Segoe UI", 32, "bold")
        )

        welcome.pack(pady=60)

        version = ctk.CTkLabel(
            self.main,
            text="Version 0.2",
            font=("Segoe UI", 20)
        )

        version.pack()


if __name__ == "__main__":
    app = FM25AIStudio()
    app.mainloop()