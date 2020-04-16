# %%
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv',
                 parse_dates=['Date'])

df = df[df['Country'].isin(['Belarus'])]
df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)
df['New_cases'] = df["Cases"].diff()

cases = px.line(df, x='Date', y='Cases', title='COVID19')
cases.show()

new_cases = px.line(df, x='Date', y='New_cases', title='COVID19')
new_cases.show()
