"""Simple GUI application that shows mouse position and copies coordinates with Ctrl+C."""

import tkinter as tk
from datetime import datetime


class MouseLocatorApp:
    """Tkinter-based app that tracks the mouse position."""

    POLL_INTERVAL_MS = 500

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Mouse Locator")
        self.root.resizable(False, False)

        self.position_label = tk.Label(
            self.root,
            text="(0, 0)",
            font=("Segoe UI", 20),
            padx=20,
            pady=20,
        )
        self.position_label.pack()

        self.status_label = tk.Label(
            self.root,
            text="Press Ctrl+C to copy coordinates",
            font=("Segoe UI", 10),
        )
        self.status_label.pack(pady=(0, 10))

        self.current_coords: tuple[int, int] = (0, 0)

        self.root.bind("<Control-c>", self.copy_coordinates)
        self.root.bind("<Control-C>", self.copy_coordinates)

    def run(self) -> None:
        self.schedule_update()
        self.root.mainloop()

    def schedule_update(self) -> None:
        self.update_position()
        self.root.after(self.POLL_INTERVAL_MS, self.schedule_update)

    def update_position(self) -> None:
        self.root.update_idletasks()
        x = self.root.winfo_pointerx()
        y = self.root.winfo_pointery()
        self.current_coords = (x, y)
        self.position_label.config(text=f"({x}, {y})")

    def copy_coordinates(self, event: tk.Event[tk.Misc]) -> None:
        coords_text = f"{self.current_coords[0]}, {self.current_coords[1]}"
        self.root.clipboard_clear()
        self.root.clipboard_append(coords_text)
        self.status_label.config(
            text=f"Copied {coords_text} at {datetime.now().strftime('%H:%M:%S')}"
        )


def main() -> None:
    MouseLocatorApp().run()


if __name__ == "__main__":
    main()
