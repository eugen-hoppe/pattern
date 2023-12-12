from enum import Enum


class UserStatus(Enum):
    ID_1 = ("Inactive", "E-Mail not confirmed", "User account is pending")
    ID_2 = ("Active", "User is active")
    ID_3 = ("Customer", "User is Customer")
    ID_4 = ("Partner", "User Service Partner")
    # ...
    ID_42 = ("Key", "UserStatus")
    # ...
    # Depricated
    # ==========
    D_ID_5 = ("Key", "UserInfo")
    # ...
