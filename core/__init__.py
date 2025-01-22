# core/__init__.py
"""Основные системные компоненты игры"""
from .settings_manager import SettingsManager
from .game_engine import GameEngine

__all__ = ['SettingsManager', 'GameEngine']