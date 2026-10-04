# gui.py

print(">>> gui.py is being imported")

from engine.game_bridge import game_callback
from engine.game_loop import start_new_game
from engine.game_loop import start_loaded_game
from engine.commands import process_command
from systems.save_load import save_game
import customtkinter as ctk
import tkinter as tk


class ToolTip:
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


THEME_BG = "#2b2b2b"
THEME_FG = "#e8e8e8"
THEME_ACCENT = "#2b2b2b"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#3c3c3c"
THEME_FONT_FAMILY = "Consolas"
THEME_FONT_SIZE = 10


def apply_theme(root):
    root.configure(fg_color=THEME_BG)


class QuietAcresGUI:
    def __init__(self, root):
        self.root = root
        root.title("Quiet Acres")
        root.geometry("900x600")
        apply_theme(root)

        self.game_name = ctk.CTkLabel(root, text="Quiet Acres", font=ctk.CTkFont(family="Helvetica", size=42), text_color=THEME_FG, width=377, height=65)
        self.game_name.place(x=262, y=91)

        self.start_new_game_btn = ctk.CTkButton(root, text="Start New Game", command=self.on_start_new_game_button_1, fg_color="#171717", font=ctk.CTkFont(family="Helvetica", size=12), text_color=THEME_ACCENT_FG, width=195, height=52)
        self.start_new_game_btn.place(x=353, y=195)
        #self.start_new_game_btn.bind("<Button-1>", self.on_start_new_game_button_1)
        ToolTip(self.start_new_game_btn, "Start a new game.")

        self.start_loaded_game = ctk.CTkButton(root, text="Start Loaded Game", command=self.on_start_loaded_game_button_1, fg_color="#171717", font=ctk.CTkFont(family="Helvetica", size=12), text_color=THEME_ACCENT_FG, width=195, height=52)
        self.start_loaded_game.place(x=353, y=260)
        #self.start_loaded_game.bind("<Button-1>", self.on_start_loaded_game_button_1)
        ToolTip(self.start_loaded_game, "Start a loaded game.")

        self.quit_btn = ctk.CTkButton(root, text="Quit", command=self.root.destroy, fg_color="#171717", font=ctk.CTkFont(family="Helvetica", size=13), text_color=THEME_ACCENT_FG, width=195, height=52)
        self.quit_btn.place(x=353, y=325)
        ToolTip(self.quit_btn, "Quit")

        self.output_box = ctk.CTkTextbox(root, fg_color="#292929", text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=765, height=480)

    def open_quiet_acres(self):
        return QuietAcresGUI2(self.root)

    def on_start_new_game_button_1(self):
        self.root.withdraw()
        game_callback("start")
        QuietAcresGUI2(self.root)

    def on_start_loaded_game_button_1(self):
        game_callback("load")
        QuietAcresGUI2(self.root)


class QuietAcresGUI2:
    def __init__(self, master):
        root = ctk.CTkToplevel(master)
        self.root = root
        root.title("Quiet Acres")
        root.geometry("800x600")
        apply_theme(root)

        self.main_menu_btn = ctk.CTkButton(root, text="Return to main menu", command=self.on_main_menu_btn, fg_color="#171717", font=ctk.CTkFont(family="Helvetica", size=12), text_color=THEME_ACCENT_FG, width=171, height=40)
        self.main_menu_btn.place(x=13, y=13)
        ToolTip(self.main_menu_btn, "Return to main menu.")
        self.main_menu_btn.bind("<Button-1>", self.on_main_menu_btn_button_1)

        self.help_label = ctk.CTkLabel(root, text="Type 'help' for a list of commands", text_color="#ffffff", fg_color="#171717", font=ctk.CTkFont(family="Helvetica", size=11), width=247, height=39)
        self.help_label.place(x=208, y=14)

        self.text_box = ctk.CTkEntry(root, font=ctk.CTkFont(family="Helvetica", size=13), fg_color=THEME_FIELD_BG, text_color=THEME_FG, width=765, height=30)
        self.text_box.place(x=18, y=560)
        self.text_box.bind("<Return>", self.on_enter)

        self.output_box = ctk.CTkTextbox(root, fg_color="#292929", text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=765, height=480)
        self.output_box.place(x=18, y=70)

        self.scroll_bar = ctk.CTkScrollbar(root, orientation="vertical", width=20, height=470)
        self.scroll_bar.place(x=760, y=80)

        self.scroll_bar.configure(command=self.output_box.yview)
        self.output_box.configure(yscrollcommand=self.scroll_bar.set)

    def on_enter(self, event):
        cmd = self.text_box.get()
        self.text_box.delete(0, tk.END)

        response = game_callback(cmd)

        self.output_box.insert("end", f"> {cmd}\n{response}\n")
        self.output_box.see("end")

    def on_main_menu_btn(self):
        self.root.withdraw()
        QuietAcresGUI(self.root)

    def on_main_menu_btn_button_1(self, event):
        self.root.withdraw()
        QuietAcresGUI(self.root)

def gui():
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = QuietAcresGUI(root)
    root.mainloop()