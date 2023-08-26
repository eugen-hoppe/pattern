"""
Case Pattern 2023

Convert camel-case to snake-case and vise versa

Util Models

Eugen Hoppe
https://github.com/eugen-hoppe
"""
import re


class To:

    # Method to convert from camel-case to snake-case
    # ===============================================
    @staticmethod
    def camel(snake: str) -> str:
        parts = snake.split('_')
        return parts[0] + ''.join(p.capitalize() for p in parts[1:])

    # Method to convert from snake-case to camel-case
    # ===============================================
    @staticmethod
    def snake(camel: str) -> str:
        return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel).lower()
