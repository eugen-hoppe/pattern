from d5.constants import Constant

from d5.constants.l1.l2 import UserStatusBool


class UserStatus(Constant):  # parent: 1.1
    ID_1 = ("Inactive", "E-Mail not confirmed", "User account is pending")
    ID_2 = ("Active", "User is active")
    ID_3 = ("Customer", "User is Customer")
    ID_4 = ("Partner", "User Service Partner")
    # ...
    ID_42 = ("Key", "UserStatus")
    # ...
    ID_456 = UserStatusBool
    #
    # Depricated
    # ==========
    D_ID_5 = ("Key", "UserInfo")
    # ...
