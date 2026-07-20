import customtkinter as ctk
import psutil

# Window settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SystemMonitor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("System Monitor v1.0")
        self.geometry("400x350")

        # Title
        self.label_title = ctk.CTkLabel(self, text="SYSTEM STATUS", font=("Consolas", 20, "bold"), text_color="#00ff00")
        self.label_title.pack(pady=20)

        # CPU Usage Indicator
        self.cpu_label = ctk.CTkLabel(self, text="CPU Usage: %0", font=("Consolas", 16))
        self.cpu_label.pack(pady=10)

        # RAM Usage Indicator
        self.ram_label = ctk.CTkLabel(self, text="RAM Usage: %0", font=("Consolas", 16))
        self.ram_label.pack(pady=10)

        # Disk Usage Indicator
        self.disk_label = ctk.CTkLabel(self, text="Disk Usage: %0", font=("Consolas", 16))
        self.disk_label.pack(pady=10)

        # Start the update function
        self.update_stats()

    def update_stats(self):
        # Fetch data (interval=0.1 gives more accurate CPU reading)
        cpu_usage = psutil.cpu_percent(interval=0.1)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        # Update labels
        self.cpu_label.configure(text=f"CPU Usage: %{cpu_usage}")
        self.ram_label.configure(text=f"RAM Usage: %{ram_usage}")
        self.disk_label.configure(text=f"Disk Usage: %{disk_usage}")

        # Change color (turn red if usage exceeds 80%)
        self.cpu_label.configure(text_color="red" if cpu_usage > 80 else "white")
        self.ram_label.configure(text_color="red" if ram_usage > 80 else "white")
        self.disk_label.configure(text_color="red" if disk_usage > 80 else "white")

        # Run again after 1 second (live monitoring)
        self.after(1000, self.update_stats)


if __name__ == "__main__":
    app = SystemMonitor()
    app.mainloop()
