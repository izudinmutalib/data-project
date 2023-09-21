import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('')
profile_report = ProfileReport(df, title='Animal Data Profiling')