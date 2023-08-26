"""
Case Pattern 2023

Converts from snake-case to camel-case and vice versa

Util Models

Eugen Hoppe
https://github.com/eugen-hoppe
"""
import re


class To:
    # Method to convert from camel-case to snake-case
    # ===============================================
    @staticmethod
    def camel(snake: str, upper_first: bool = False) -> str:
        if snake.startswith("_"):
            snake = snake[1:]
        parts = snake.lower().split("_")
        if upper_first:
            return "".join(p.capitalize() for p in parts)
        return parts[0] + "".join(p.capitalize() for p in parts[1:])

    # Method to convert from snake-case to camel-case
    # ===============================================
    @staticmethod
    def snake(camel: str) -> str:
        return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", camel).lower()
