from d5.constants import Constant


KEY = "status"


class UserStatusBool(Constant):  # parent 1.1.456
    ID_1 = (KEY, True, "active")
    ID_2 = (KEY, False, "not active")
    # .       |         |
    # Address |         |
    #         V         V
    # .  1.1.456.2  1.1.456.2.1
