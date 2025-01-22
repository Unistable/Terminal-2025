import curses
import time

class BorderAnimation:
    def __init__(self):
        self.last_blink = time.time()
    
    def update(self, stdscr):
        current_time = time.time()
        if current_time - self.last_blink > 0.5:
            self._draw_blinking(stdscr)
            self.last_blink = current_time

    def _draw_blinking(self, stdscr):
        h, w = stdscr.getmaxyx()
        for y in [0, h-1]:
            for x in range(1, w-1):
                try:
                    stdscr.addch(y, x, '*' if time.time() % 1 < 0.5 else ' ', curses.color_pair(1))
                except curses.error:
                    pass