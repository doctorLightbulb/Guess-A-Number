# guess_a_number.py

__version__ = "2.0"

import tkinter as tk
from tkinter import Frame, Label, StringVar


class MainWindow(tk.Tk):
    """The main window for the guessing game."""

    def __init__(self):
        super().__init__()

        # Window settings:
        self.title("Guess-A-Number")

        # Screen orientation
        center_x = self.winfo_screenwidth() // 2
        center_y = self.winfo_screenheight() // 2
        window_width = 400
        window_height = 300
        x = center_x - window_width // 2
        y = center_y - window_height // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Game variables
        self.message = StringVar(self, value="Welcome!")

        # UI
        self.UI()

        # Key bindings
        self.bindings()

    def bindings(self):
        pass

    def UI(self):
        self.main_frame = Frame(self)
        self.main_frame.pack()

        self.message_label = Label(
            self.main_frame,
            textvariable=self.message,
        )
        self.message_label.pack()


def main():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
