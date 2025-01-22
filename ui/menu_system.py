import curses
from typing import List
from ui.sound_manager import SoundManager
from core.settings_manager import SettingsManager

class MenuSystem:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.sound_manager = SoundManager()
        self.settings_manager = SettingsManager()
        self.current_row = 0
        self.menu_items = ["Start Game", "Settings", "Exit"]
        self.init_colors()

    def init_colors(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def draw_menu(self):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        
        # Draw title
        title = "TERMINAL 2025"
        self.stdscr.addstr(h // 2 - 4, w // 2 - len(title) // 2, title, curses.color_pair(1))
        
        # Draw menu items
        for idx, item in enumerate(self.menu_items):
            x = w // 2 - len(item) // 2
            y = h // 2 - 2 + idx
            attr = curses.color_pair(1) | curses.A_BOLD if idx == self.current_row else curses.color_pair(2)
            self.stdscr.addstr(y, x, f"{'>' if idx == self.current_row else ' '} {item}", attr)
        
        self.stdscr.refresh()

    def handle_input(self):
        key = self.stdscr.getch()
        if key == curses.KEY_UP and self.current_row > 0:
            self.current_row -= 1
            self.sound_manager.play("navigate")
        elif key == curses.KEY_DOWN and self.current_row < len(self.menu_items) - 1:
            self.current_row += 1
            self.sound_manager.play("navigate")
        return key

    def run(self):
        while True:
            self.draw_menu()
            key = self.handle_input()
            if key in [curses.KEY_ENTER, 10, 13]:
                self.sound_manager.play("select")
                return self.current_row