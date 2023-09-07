from dataclasses import dataclass
from pprint import pprint

import case


SQL = (
    "SELECT {first_name}, {last_name}, {user_mail} FROM user"
    + " WHERE {user_mail} = {where_0}"
)
EXAMPLE = {
    "columns": ("userId", "firstName", "lastName", "userMail"),
    "rows": [
        (42, "Arthur", "Dent", "ad@example.com")
    ]
}


@dataclass
class User42:
    user_id: int = 42
    first_name: str = "Arthur"
    last_name: str = "Dent"
    user_mail: str = "ad@example.com"

    @staticmethod
    def columns() -> dict[str, str]:
        table_columns: dict[str, str] = {}
        for key in User42.__annotations__:
            table_columns[key] = case.To.camel(key)
        return table_columns


if __name__ == "__main__":
    """Examples of method usage
    
    Methods:
      - case.To.snake()
      - case.To.camel()
    """
    db_columns = User42.columns()
    print("Equivalent mapping")
    pprint(db_columns, indent=4)
    query = SQL.format(where_0 ="ad@example.com", **db_columns)
    print("SQL Statement:", query, "\n")
    for row in EXAMPLE["rows"]:
        kwargs = dict()
        for index, column in enumerate(EXAMPLE["columns"]):
            kwargs[case.To.snake(column)] = row[index]
            print(f"Column No.{index+1}:", column, case.To.snake(column))

        update_user = User42(**kwargs)
        update_user.user_mail = "a.dent@example.com"
    print("Updated object for next operations:", update_user, "\n")
