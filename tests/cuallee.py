from datetime import date, datetime
import pandas as pd
from cuallee import Control, Check, CheckLevel

df = pd.DataFrame({"X": [None, 2, 3], "Y": [10, 20, 30]})
# Checks all columns in dataframe for using is_complete check
type(Control.completeness(df))

check = Check(CheckLevel.ERROR, "Not Null", execution_date=datetime.now())

(check.is_complete(("X")).is_complete(("Y")).is_between(("Y"), value=(10, 20)).validate(df))
