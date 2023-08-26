from casepat import case


TEST_1 = {
    "first_name": "firstName",
    "company_address": "companyAddress",
    "account_user_id": "accountUserId",
}
TEST_2 = {
    "first_name": "FirstName",
    "company_address": "CompanyAddress",
    "account_user_id": "AccountUserId",
}
TEST_3 = {
    "FirstName": "first_name",
    "company_Address": "company_address",
    "account_user_id": "account_user_id",
}
TEST_4 = {
    "first_Name": "firstName",
    "Company_Address": "companyAddress",
    "account_user_id_": "accountUserId",
    "_account_user_id": "accountUserId",
    "": "",
}


def test_camel_snake():
    """Test camel/snake case conversion"""
    for snake, camel in TEST_1.items():
        assert case.To.camel(snake) == camel
        assert case.To.snake(camel) == snake


def test_camel_snake_upper_first():
    """Test camel/snake case conversion with upper_first=True"""
    for snake, camel in TEST_2.items():
        assert case.To.camel(snake, True) == camel
        assert case.To.snake(camel) == snake


def test_unusual_camel_to_snake():
    """Test camel/snake case conversion with unusual cases"""
    for camel, snake in TEST_3.items():
        assert case.To.snake(camel) == snake


def test_unusual_snake_to_camel():
    """Test camel/snake case conversion with unusual cases"""
    for snake, camel in TEST_4.items():
        assert case.To.camel(snake) == camel
