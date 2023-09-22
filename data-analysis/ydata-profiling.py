import pandas as pd
from ydata_profiling import ProfileReport

# Test on small size file
df = pd.read_csv('/workspace/data-project/data-analysis/spotify_most_streamed_copy.csv', engine='pyarrow', dtype_backend='pyarrow')
profile_report = ProfileReport(df, title='First Data Profiling', explorative=True)

df = pd.read_csv('/workspace/data-project/data-analysis/spotify_most_streamed_copy.csv', engine='pyarrow', dtype_backend='pyarrow')
profile2_report = ProfileReport(df, title='Second Data Profiling', explorative=True)

comparison_report = profile_report.compare(profile2_report)
comparison_report.to_file('compare.html')