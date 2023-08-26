from casepat import case


TEST_1 = {
    "first_name": "firstName",
    "company_address": "companyAddress"
}
TEST_2 = {
    "FirstName": "first_name",
    "CompanyAddress": "company_address"
}

def test_camel_snake():
    for snake, camel in TEST_1.items():
        assert case.To.camel(snake) == camel
        assert case.To.snake(camel) == snake


def test_camel_starts_with_upper_char():
    for camel, snake in TEST_2.items():
        assert case.To.snake(camel) == snake
