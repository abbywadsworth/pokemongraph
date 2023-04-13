import pandas as pd
import plotly.express as px
import streamlit as st



# Load the data
df = pd.read_csv('pokemonclean.csv')

#getting rid of percentage_male
pokemon.drop(labels='percentage_male', axis=1, inplace=True)



# Define the available generations
gen = list(df['Generation'].unique())
gen.append('All')



# Define the available types
types = list(df['Primary'].unique())
types.append('All')




years = list(df['Year'].unique())

# Define the Streamlit app
st.title('Graph your own Pokemon data')

selected_gen = st.selectbox('Select a generation', gen)
selected_type = st.selectbox('Select a type', types)

#making the figures
if selected_gen == 'All':
    df_gen = df
else:
    df_gen = df[df['Generation'] == selected_gen]

fig = px.scatter(df_gen[df_gen['Generation']==selected_gen],
                 x='Weight',y='Height', color='Region',
                 hover_data=['Name'], size='HP')
fig.update_layout(title=f'Weight vs Height for {selected_type} in Generation {selected_gen}')

#telling streamlit you have a plotly fig to insert
st.plotly_chart(fig)
