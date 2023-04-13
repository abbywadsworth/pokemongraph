import pandas as pd
import plotly.express as px
import streamlit as st



# Load the data
df = pd.read_csv('cleanpokemon.csv')

#getting rid of percentage_male
#df.drop(labels='percentage_male', axis=1, inplace=True)



# Define the available generations
gen = list(df['Generation'].unique())
gen.append('All')



# Define the available types
types = list(df['Primary'].unique())
types.append('All')




#years = list(df['Year'].unique())

# Define the Streamlit app
st.title('Graph your own Pokemon data')


#making drop down menus
selected_gen = st.selectbox('Select a generation', gen)
selected_type = st.selectbox('Select a type', types)

#making the figures
if selected_gen == 'All':
    df_gen = df
else:
    df_gen = df[df['Generation'] == selected_gen]
    
if selected_type == 'All':
    df_gen = df
else:
    df_gen = df[df['Primary'] == selected_type]

    
    
colours = {
'Normal': '#A8A77A',
'Fire': '#EE8130',
'Water': '#6390F0',
'Electric': '#F7D02C',
'Grass': '#7AC74C',
'Ice': '#96D9D6',
'Fighting': '#C22E28',
'Poison': '#A33EA1',
'Ground': '#E2BF65',
'Flying': '#A98FF3',
'Psychic': '#F95587',
'Bug': '#A6B91A',
'Rock': '#B6A136',
'Ghost': '#735797',
'Dragon': '#6F35FC',
'Dark': '#705746',
'Steel': '#B7B7CE',
'Fairy': '#D685AD',
}    
    
    
    
    
    
fig = px.scatter(df_gen[df_gen['Generation']==selected_gen],
                 x='Weight',y='Height', color_discrete_map=colours,
                 hover_data='Name', size='HP')
fig.update_layout(title=f'Weight vs Height for {selected_type} in Generation {selected_gen}')

#telling streamlit you have a plotly fig to insert
st.plotly_chart(fig)
