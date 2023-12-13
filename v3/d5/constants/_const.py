from enum import Enum


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
