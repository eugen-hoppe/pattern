from d5.constants import Constant


class UserStatusBool(Constant):  # parent 1.1.456
    ID_1 = (True, "active")
    ID_2 = (False, "not active")
    # .       |         |
    # Address |         |
    #         V         V
    # .  1.1.456.2  1.1.456.2.1
