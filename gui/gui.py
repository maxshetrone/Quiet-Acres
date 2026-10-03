# gui.py


import customtkinter as ctk
import tkinter as tk


class QuietAcresGUI(ctk.CTk):
    def __init__(self, widget, text, delay=500):
        self.widget = widget
        self.text = text
        self.delay = delay
        self.tip = None
        self._job = None
        # add="+" so this never replaces bindings the widget already has.
        widget.bind("<Enter>", self._schedule, add="+")
        widget.bind("<Leave>", self._hide, add="+")
        widget.bind("<ButtonPress>", self._hide, add="+")

    def _schedule(self, _event=None):
        self._cancel()
        self._job = self.widget.after(self.delay, self._show)

    def _cancel(self):
        if self._job is not None:
            self.widget.after_cancel(self._job)
            self._job = None

    def _show(self):
        if self.tip is not None:
            return
        x = self.widget.winfo_rootx() + 12
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
        self.tip = tk.Toplevel(self.widget)
        # No title bar or border — it should look like a tooltip, not a window.
        self.tip.wm_overrideredirect(True)
        self.tip.wm_geometry(f"+{x}+{y}")
        tk.Label(
            self.tip,
            text=self.text,
            justify="left",
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            padx=6,
            pady=3,
        ).pack()

    def _hide(self, _event=None):
        self._cancel()
        if self.tip is not None:
            self.tip.destroy()
            self.tip = None


THEME_BG = "#1a1414"
THEME_FG = "#dbdbdb"
THEME_ACCENT = "#0b0a0a"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#3c3c3c"
THEME_FONT_FAMILY = "Consolas"
THEME_FONT_SIZE = 10


def apply_theme(root):
    root.configure(fg_color=THEME_BG)


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Quiet Acres")
        root.geometry("800x600")
        apply_theme(root)

        self.return_to_menu = ctk.CTkButton(root, text="Click to return to Menu", command=self.on_return_to_menu, text_color="#f2f2f2", font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), fg_color=THEME_ACCENT, corner_radius=0, width=172, height=32)
        self.return_to_menu.place(x=5, y=5)
        ToolTip(self.return_to_menu, "Click to return to menu. Or type ` to return to menu.")

        self.text_box = ctk.CTkEntry(root, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), fg_color=THEME_FIELD_BG, text_color=THEME_FG, corner_radius=0, width=765, height=26)
        self.text_box.place(x=13, y=559)
        ToolTip(self.text_box, "Type command.")

        self.help_text = ctk.CTkLabel(root, text="Type 'help' to show all commands.", text_color="#f2f2f2", fg_color="#0b0a0a", font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), corner_radius=0, width=273, height=32)
        self.help_text.place(x=195, y=5)

        self.version_number = ctk.CTkButton(root, text="Version: ", command=self.on_version_number, text_color="#f2f2f2", font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), fg_color=THEME_ACCENT, corner_radius=0, width=140, height=32)
        self.version_number.place(x=650, y=5)
        ToolTip(self.version_number, "Click to open Github.")

        self.output_box = ctk.CTkTextbox(root, fg_color="#000000", text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=765, height=494)
        self.output_box.place(x=13, y=53)

    def on_return_to_menu(self):
        pass

    def on_version_number(self):
        pass


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = Application(root)
    root.mainloop()