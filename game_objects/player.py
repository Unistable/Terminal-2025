import curses
from typing import Tuple
from utils.helpers import clamp_value

class Player:
    def __init__(self, start_x: int, start_y: int):
        self.x, self.y = start_x, start_y
        self.characters = ['@', '>', '<', '^', 'v']
        self.current_frame = 0
        self.color_pair = 2

    def update_appearance(self, color_pair: int):
        self.color_pair = color_pair

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def move_up(self): 
        self.move(0, -1)
    
    def move_down(self): 
        self.move(0, 1)
    
    def move_left(self): 
        self.move(-1, 0)
    
    def move_right(self): 
        self.move(1, 0)

    def draw(self, stdscr):
        h, w = stdscr.getmaxyx()
        self.x = clamp_value(self.x, 1, w-2)
        self.y = clamp_value(self.y, 1, h-2)
        
        try:
            char = self.characters[self.current_frame % 4 + 1] if self.current_frame > 0 else self.characters[0]
            stdscr.addch(self.y, self.x, char, curses.color_pair(self.color_pair))
            self.current_frame = (self.current_frame + 1) % 8 if self.current_frame > 0 else 0
        except curses.error:
            pass