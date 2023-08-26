from casepat import case


TEST_1 = {
    "first_name": "firstName",
    "company_address": "companyAddress"
}
TEST_2 = {
    "FirstName": "first_name",
    "company_Address": "company_address",
    "account_user_id": "account_user_id",
}


def test_camel_snake():
    for snake, camel in TEST_1.items():
        assert case.To.camel(snake) == camel
        assert case.To.snake(camel) == snake


def test_unusual_camel_to_snake():
    for camel, snake in TEST_2.items():
        assert case.To.snake(camel) == snake
