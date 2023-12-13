import os
import re
from enum import Enum


# Configuration
# =============
PATH_TO_INIT_FILE = ["v3", "d5", "constants"]
CONSTANT_NAMES = (
    "account",
    "user",
)
# TODO: for sub constants


# Main module
# ===========
class Constant(Enum):
    """
    Constant Instance

    Imports are registered in:
      - d5 / constants / __init__.py
      - d5 / constants / sub / __init__.py
    """

    @classmethod
    def fetch(cls, addr: list | str, **_):
        if isinstance(addr, str):
            addr = [int(id_) for id_ in addr.split(".")]
        cache: Enum = cls
        for id in addr:
            if isinstance(cache, tuple):
                return cache[id]
            node: Enum = getattr(cache, "ID_" + str(id))
            cache = node.value
        return cache[0]

    @staticmethod
    def init_file(const_names: list, path: list[str] = PATH_TO_INIT_FILE):
        snippet = "from d5.constants._const import Constant\n\n"
        class_names = ["Constant"]
        for name in const_names:
            class_name = To.camel(name, True)
            snippet += f"from d5.constants.{name} import {class_name}\n"
            class_names.append(class_name)
        snippet += "\n\n__all__ = (\n"
        for cls_name in class_names:
            snippet += " " * 4 + f'"{cls_name}",\n'
        snippet += ")\n"

        with open(file=os.path.join(*path, f"__init__.py"), mode="w") as file_py:
            file_py.write(snippet)


# Dependency Pattern
# ==================
class To:
    """
    Casepat: https://github.com/eugen-hoppe/pattern/tree/main/v3/casepat
    """

    @staticmethod
    def camel(snake: str, upper_first: bool = False) -> str:
        if snake.startswith("_"):
            snake = snake[1:]
        parts = snake.lower().split("_")
        if upper_first:
            return "".join(p.capitalize() for p in parts)
        return parts[0] + "".join(p.capitalize() for p in parts[1:])

    @staticmethod
    def snake(camel: str) -> str:
        return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", camel).lower()


if __name__ == "__main__":
    Constant.init_file(CONSTANT_NAMES)
