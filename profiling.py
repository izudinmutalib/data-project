import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('spotify_most_streamed.csv')
profile_report = ProfileReport(df, title='Spotify Data Profiling')
profile_report.to_file('report.html')