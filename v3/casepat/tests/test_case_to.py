from casepat import case


TEST_1 = {
    "first_name": "firstName",
    "company_address": "companyAddress"
}


def test_camel_snake():
    for snake, camel in TEST_1.items():
        assert case.To.camel(snake) == camel
        assert case.To.snake(camel) == snake
