# CSV Const

## TODO: DOC

```python
import os

import pandas as pd


# Location of CSV to create py-file for constants
# ===============================================
PATH, FILE = ["data", "exoplanet"], "exoplanet_eu_catalog"  # .csv


# Name of the enum-class for CSV columns
# ======================================
ENUM = "X"  # X-Axis


def create(
    path: list[str] = PATH,
    file: str = FILE,
    snippet: str = "@unique\nclass {0}(str, Enum):\n".format(ENUM),
    i4: str = "    ",
) -> None:
    """
    Create constants from columns of a CSV file.
    """
    try:
        csv_path = os.path.join(*path, f"{file}.csv")
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found at {csv_path}")
        snippet = "from enum import Enum, unique\n\n\n" + snippet
        snippet += (  # docstring
            f'{i4}"""\n{i4}Column Names as Constants of: {csv_path}\n\n'
            + f'{i4}Created with: "https://github.com/eugen-hoppe/pattern"\n{i4}"""\n'  # TODO update subpath
        )
        for col in pd.read_csv(csv_path).columns:
            snippet += f'{i4}{col.upper()}: str = "{col}"\n'

        snippet += (
            f'\n{i4}@staticmethod\n{i4}def path():\n{i4}{i4}return "{csv_path}"\n'
        )
        output_path = os.path.join(*path, f"{file}.py")
        with open(file=output_path, mode="w") as file_py:
            file_py.write(snippet)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except pd.errors.ParserError:
        print(f"Error reading the CSV file at {csv_path}. Please check its format.")
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    create()

```
