from d5.dictionary import App, constants


if __name__ == "__main__":
    # Example

    # encoded data from db: 1.1.3 ->
    addr_1_1_3 = App.ID_1.value.ID_1.value.ID_3.value[0]
    print(addr_1_1_3)

    # encoded data from db: 1.1.3.1 ->
    addr_1_1_3_1 = App.ID_1.value.ID_1.value.ID_3.value[1]
    print(addr_1_1_3_1)

    # encoded data from db: 2.1.2.1 ->
    print(App.fetch([2, 1, 2, 1]))

    # encoded data from db: 1.1.42.1 ->
    print(App.fetch("1.1.42.1"))

    # encoded data from db: (1.)1.42.1 ->
    print(constants.User.fetch("1.42.1"))

    # encoded data
    print(App.fetch("1.1.456.2.1"))
