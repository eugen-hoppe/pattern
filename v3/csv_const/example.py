import pandas as pd

from data.exoplanet.exoplanet_eu_catalog import X  # [0]


# [0] BEFORE IMPORT: Create Constants from CSV File
# =================================================
# - a: adapt constants in csv_const.py (optional)
# - b: run 'python csv_const.py'
# - c: check 'exoplanet_eu_catalog.py' is appeared
# - d: use as import
# -------------------------------------------------


# [1] Get path with path()-method
# ===============================
df = pd.read_csv(X.path())


# [2] Access columns with the dot syntax
# ======================================
df = df.dropna(subset=X.DISCOVERED)  # X.{COLUMN}


# [3] Work with X-Enum
df[X.DISCOVERED] = [int(year) for year in df[X.DISCOVERED]]

print(df.groupby(by=X.DISCOVERED)[X.DISCOVERED].count().head(10))
