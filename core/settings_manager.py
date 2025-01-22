import json
import curses
from pathlib import Path
from typing import Dict, Any

class SettingsManager:
    COLOR_SCHEMES = {
        "classic": (curses.COLOR_CYAN, curses.COLOR_GREEN),
        "cyberpunk": (curses.COLOR_GREEN, curses.COLOR_YELLOW),
        "retro": (curses.COLOR_YELLOW, curses.COLOR_RED)
    }

    def __init__(self):
        self.settings_file = Path("settings.json")
        self.settings = self.load()

    def load(self) -> Dict[str, Any]:
        """Загружает настройки из файла"""
        try:
            if self.settings_file.exists():
                with open(self.settings_file, 'r') as f:
                    return {**self.get_default_settings(), **json.load(f)}
            return self.get_default_settings()
        except Exception as e:
            print(f"Error loading settings: {e}")
            return self.get_default_settings()

    def save(self) -> None:
        """Сохраняет текущие настройки в файл"""
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=2)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def get_default_settings(self):
        return {
            "color_scheme": "classic",
            "sound_enabled": True,
            "controls": {"up": "w", "down": "s", "left": "a", "right": "d"}
        }

    def configure(self, stdscr) -> None:
        """Интерактивная настройка параметров"""
        curses.curs_set(0)
        current_selection = 0
        options = [
            ("Color Scheme", self._change_color_scheme),
            (f"Sound Effects: {'ON' if self.settings['sound_enabled'] else 'OFF'}", self._toggle_sound),
            ("Save and Exit", lambda: None)
        ]

        while True:
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            
            stdscr.addstr(0, 0, "SETTINGS MENU", curses.color_pair(1) | curses.A_BOLD)
            for idx, (label, _) in enumerate(options):
                x = w // 2 - len(label) // 2
                y = h // 2 - len(options) // 2 + idx
                prefix = "> " if idx == current_selection else "  "
                stdscr.addstr(y, x, f"{prefix}{label}", curses.color_pair(1) if idx == current_selection else curses.color_pair(2))

            key = stdscr.getch()
            if key == curses.KEY_UP and current_selection > 0:
                current_selection -= 1
            elif key == curses.KEY_DOWN and current_selection < len(options) - 1:
                current_selection += 1
            elif key in [curses.KEY_ENTER, 10, 13]:
                if current_selection == len(options) - 1:
                    self.save()
                    break
                options[current_selection][1](stdscr)
                if current_selection == 1:
                    options[1] = (f"Sound Effects: {'ON' if self.settings['sound_enabled'] else 'OFF'}", self._toggle_sound)

    def _change_color_scheme(self, stdscr) -> None:
        current = self.settings["color_scheme"]
        schemes = list(self.COLOR_SCHEMES.keys())
        new_scheme = schemes[(schemes.index(current) + 1) % len(schemes)]
        self.settings["color_scheme"] = new_scheme
        self.apply_color_scheme()
        stdscr.refresh()

    def _toggle_sound(self, stdscr) -> None:
        self.settings["sound_enabled"] = not self.settings["sound_enabled"]

    def apply_color_scheme(self):
        colors = self.COLOR_SCHEMES[self.settings["color_scheme"]]
        curses.init_pair(1, colors[0], curses.COLOR_BLACK)
        curses.init_pair(2, colors[1], curses.COLOR_BLACK)