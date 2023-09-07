# Documentation

This pattern contains two Python files: one called `case.py` which defines a class `To` with static methods for converting between camelCase and snake_case, and another file which uses this `case` module to demonstrate different ways of working with a dataclass and for example an SQL query template.

Let's break down how the `case` module works and how it's used in this script:

### `case.py`:

#### Method `To.camel`:

- **Input**: A snake_case string (optionally starting with "_") and a boolean indicating whether to capitalize the first letter.
- **Output**: The input string converted to camelCase.
- **How it works**: 
  - It removes a leading underscore if there is one.
  - It splits the string into parts using "_" as the delimiter.
  - It joins the parts together, capitalizing the first letter of each part except the first one (or all parts if `upper_first` is True).

#### Method `To.snake`:

- **Input**: A camelCase string.
- **Output**: The input string converted to snake_case.
- **How it works**: 
  - It uses a regex substitution to insert underscores before each uppercase letter (that follows a lowercase letter or digit), and then converts the whole string to lowercase.


Overall, this `example.py` showcases how to use the `case` module to work with dataclasses and SQL queries in a way that allows for conversion between camelCase and snake_case.

## LINKS

### example.py

- [Commit with comments](https://github.com/eugen-hoppe/pattern/blob/25e7df01c6fe158a11ef6375ec9ef2c8ee165cca/v3/casepat/example.py)
