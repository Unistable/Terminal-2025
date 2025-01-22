import curses
from ui.menu_system import MenuSystem
from core.game_engine import GameEngine
from core.settings_manager import SettingsManager

class Application:
    def __init__(self):
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.load()

    def run(self):
        curses.wrapper(self.main_loop)

    def main_loop(self, stdscr):
        while True:
            menu = MenuSystem(stdscr)
            choice = menu.run()
            
            if choice == 0:
                try:
                    game = GameEngine(stdscr, self.settings)
                    game.run()
                except Exception as e:
                    stdscr.addstr(0, 0, f"Error: {str(e)}")
                    stdscr.getch()
            elif choice == 1:
                self.settings_manager.configure(stdscr)
                self.settings = self.settings_manager.load()
            else:
                break

if __name__ == "__main__":
    app = Application()
    app.run()