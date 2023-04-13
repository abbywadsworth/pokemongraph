import pandas as pd
import plotly.express as px
import streamlit as st

pokemon.drop(labels='height_m', axis=1, inplace=True)

# Load the data
df = pd.read_csv('pokemonclean.csv')
df = df.dropna(subset='population')



# Define the available regions
regions = list(df['Region'].unique())
regions.append('All')

years = list(df['Year'].unique())

# Define the Streamlit app
st.title('World Data Explorer')

selected_region = st.selectbox('Select a region', regions)
selected_year = st.selectbox('Select a year', years)

#making the figures
if selected_region == 'All':
    df_region = df
else:
    df_region = df[df['Region'] == selected_region]

fig = px.scatter(df_region[df_region['Year']==selected_year],
                 x='gdp',y='life_expectancy', color='Region',
                 hover_data=['Country Name'], size='population')
fig.update_layout(title=f'GDP vs Life Expectancy for {selected_region} in {selected_year}')

#telling streamlit you have a plotly fig to insert
st.plotly_chart(fig)
