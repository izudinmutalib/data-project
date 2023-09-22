import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('/workspace/data-project/data-analysis/spotify_most_streamed.csv')
profile_report = ProfileReport(df, title='Spotify Data Profiling', explorative=True)

df = pd.read_csv('/workspace/data-project/data-analysis/spotify_most_streamed copy.csv')
profile2_report = ProfileReport(df, title='Spotify profiling 2', explorative=True)

comparison_report = profile_report.compare(profile2_report)
comparison_report.to_file('compare.html')