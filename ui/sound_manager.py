import platform
import winsound
import os

class SoundManager:
    def __init__(self):
        self.system = platform.system()
        self.sounds = {
            "navigate": (800, 100),
            "select": (1200, 200),
            "error": (400, 300)
        }

    def play(self, sound_type: str):
        if self.system == "Windows":
            freq, duration = self.sounds.get(sound_type, (440, 200))
            winsound.Beep(freq, duration)
        else:
            # Для Linux/Mac можно использовать звуковые команды
            os.system(f"play -n synth {duration/1000} sin {freq} >/dev/null 2>&1")