import curses
from typing import Dict, Any
from game_objects.player import Player
from ui.animations import BorderAnimation

class GameEngine:
    MIN_HEIGHT, MIN_WIDTH = 24, 60  # Минимальные размеры окна

    def __init__(self, stdscr, settings: Dict[str, Any]):
        self.stdscr = stdscr
        self.settings = settings
        self.is_running = True
        self.player = Player(*self._get_initial_position())
        self.border_anim = BorderAnimation()
        self.init_colors()
        self._check_window_size()

    def _get_initial_position(self) -> tuple:
        """Возвращает стартовую позицию игрока по центру"""
        h, w = self.stdscr.getmaxyx()
        return (w//2, h//2)

    def _check_window_size(self):
        """Проверяет размер окна при инициализации"""
        h, w = self.stdscr.getmaxyx()
        if h < self.MIN_HEIGHT or w < self.MIN_WIDTH:
            raise ValueError("Window too small")

    def init_colors(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Границы
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Игрок
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Текст

    def handle_input(self, key: int):
        controls = self.settings["controls"]
        if key == ord(controls["up"]): 
            self.player.move_up()
        elif key == ord(controls["down"]): 
            self.player.move_down()
        elif key == ord(controls["left"]): 
            self.player.move_left()
        elif key == ord(controls["right"]): 
            self.player.move_right()
        elif key == 27: 
            self.is_running = False

    def render(self):
        self.stdscr.clear()
        self._draw_borders()
        self.player.draw(self.stdscr)
        self.stdscr.refresh()

    def _draw_borders(self):
        """Отрисовка статических границ комнаты"""
        h, w = self.stdscr.getmaxyx()
        for y in range(h):
            for x in range(w):
                if y == 0 or y == h-1 or x == 0 or x == w-1:
                    try:
                        self.stdscr.addch(y, x, '#', curses.color_pair(1))
                    except curses.error:
                        pass

    def run(self):
        while self.is_running:
            self.render()
            key = self.stdscr.getch()
            self.handle_input(key)