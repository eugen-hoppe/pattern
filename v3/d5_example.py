from pydantic import BaseModel

from d5.dictionary import App, constants


class ApiUser(BaseModel):
    status: str = App.fetch("1.1.456.2.2")


if __name__ == "__main__":
    # Examples
    # ========================================================================

    # Example 1 (1.1.3)
    addr_1_1_3 = App.ID_1.value.ID_1.value.ID_3.value[0]
    print(addr_1_1_3)  # -> Customer

    # Example 2 (1.1.3.1)
    addr_1_1_3_1 = App.ID_1.value.ID_1.value.ID_3.value[1]
    print(addr_1_1_3_1)  # -> User is Customer

    # Example 3 (2.1.2.1)
    print(App.fetch([2, 1, 2, 1]))  # -> Paid Plan

    # Example 4a (1.1.42.1)
    print(App.fetch("1.1.42.1"))  # -> UserStatus

    # Example 4b (_.1.42.1)
    print(constants.User.fetch("1.42.1"))  # -> [1.1.42.1]

    # Example 4c (_.1.42.1.0)
    print(constants.User.fetch("1.42.1.0"))  # -> [1.1.42.1]

    # Example 6
    print(App.fetch("1.1.456.2.1"))  # -> False

    # Example 7
    print()
    user_api = ApiUser()
    user_api_dict = user_api.model_dump()
    print(user_api_dict)  # -> {'status': 'not active'}

    print()

    encoded_key = "1.1.456.2"
    encoded_value = "1.1.456.2.2"

    user_api_encode = {encoded_key: encoded_value}
    print(user_api_encode)  # -> {'1.1.456.2': '1.1.456.2.2'}

    print()

    print("decode", "=" * 20)
    print(encoded_key, "=>", App.fetch(encoded_key))
    print(encoded_value, "=>", App.fetch(encoded_value))
    print("decode", "-" * 20)  # ->

    # decode ====================
    # 1.1.456.2 => status
    # 1.1.456.2.2 => not active
    # decode --------------------
