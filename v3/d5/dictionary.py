from enum import Enum

from d5 import constants  # NOTE: dd_dict / constants / __init__.py



class App(Enum):  # or Project, Domain etc.
    ID_1 = constants.User
    ID_2 = constants.Account
    # ...
    
    @staticmethod
    def fetch(addr: list | str):
        # TODO: create Enum Mixin with methods to access values by address

        if isinstance(addr, str):
            raise NotImplementedError("TODO str address like 1.2.1")
        cache: Enum = App
        for id in addr:
            if isinstance(cache, tuple):
                return cache[id]
            node: Enum = getattr(cache, "ID_" + str(id))
            cache = node.value
        return cache[0]
