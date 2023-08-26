"""
Case Pattern 2023

Convert camel-case to snake-case and vise versa

Util Models

Eugen Hoppe
https://github.com/eugen-hoppe
"""

class To:

    # Method to convert form camel-case to snake-case
    # ===============================================
    @staticmethod
    def camel(snake: str) -> str:
        parts = snake.split('_')
        return parts[0] + ''.join(p.capitalize() for p in parts[1:])

    # Method to convert form snake-case to camel-case
    # ===============================================
    @staticmethod
    def snake(camel: str) -> str:
        chars = ['_' + ch.lower() if ch.isupper() else ch for ch in camel]
        return ''.join(chars).lstrip('_')
