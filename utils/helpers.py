from typing import Any, Union
import json

def validate_input(value: Any, expected_type: type) -> bool:
    """Проверяет соответствие значения ожидаемому типу"""
    return isinstance(value, expected_type)

def clamp_value(value: Union[int, float], 
               min_val: Union[int, float], 
               max_val: Union[int, float]) -> Union[int, float]:
    """Ограничивает значение в заданном диапазоне"""
    return max(min_val, min(value, max_val))

def calculate_center_position(stdscr, text_length: int) -> int:
    """Рассчитывает центральную позицию для текста"""
    _, width = stdscr.getmaxyx()
    return (width // 2) - (text_length // 2)

def load_json_file(file_path: str) -> dict:
    """Безопасно загружает JSON файл"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}