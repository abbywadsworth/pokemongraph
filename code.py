import pandas as pd
import plotly.express as px
import streamlit as st



# Load the data
df = pd.read_csv('cleanpokemon.csv')

#getting rid of percentage_male
#df.drop(labels='percentage_male', axis=1, inplace=True)


# Define the Streamlit app
st.title('Graph your own Pokemon data')


# Define the available generations
gen = list(df['Generation'].unique())
gen.append('Legendary')
gen.append('All')



# Define the available types
types = list(df['Primary'].unique())
types.append('All')



#making drop down menus
selected_gen = st.selectbox('Select a generation', gen)
selected_type = st.selectbox('Select a type', types)

#making the figures
if selected_gen == 'All':
    df_gen = df
elif selected_gen == 'Legendary':
    df_gen = df[df['Legendary'] == True]
else:
    df_gen = df[df['Generation'] == selected_gen]
    
    
if selected_type == 'All':
    df_gen = df
else:
    df_gen = df[df['Primary'] == selected_type]

x = ['Height', 'HP', 'MaxHP', 'Stamina', 'Weight']
    
selected_x = st.selectbox('Select a variable for your x-axis',x)

y = ['Height', 'HP', 'MaxHP', 'Stamina', 'Weight']

selected_y = st.selectbox('Select a variable for your y-axis',y)



size = ['Height', 'HP', 'MaxHP', 'Stamina', 'Weight']
gen.append('None')

selected_size = st.selectbox('Select a variable for your size',size)



    
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
    

if selected_size == 'None':
    if selected_gen == 'All':
        fig = px.scatter(df_gen,
                 x=selected_x,y=selected_y, color='Primary',
                 color_discrete_map=colours, hover_data='Name')
        fig.update_layout(title=f'{selected_x} vs {selected_y} for {selected_type} Pokemon from all Generations')

    
    elif selected_gen == 'Legendary':
        fig = px.scatter(df_gen[df_gen['Legendary']==True],
                 x=selected_x,y=selected_y, color='Primary',
                 color_discrete_map=colours, hover_data='Name')
        if selected_type == 'All':
            fig.update_layout(title=f'{selected_x} vs {selected_y} for {selected_type} Legendary Pokemon')
    
        else:
            fig.update_layout(title=f'{selected_x} vs {selected_y} for Legendary {selected_type} Pokemon')

    
    else:
        fig = px.scatter(df_gen[df_gen['Generation']==selected_gen],
                 x=selected_x,y=selected_y, color='Primary',
                 color_discrete_map=colours, hover_data='Name')
        fig.update_layout(title=f'{selected_x} vs {selected_y} for {selected_type} Pokemon in Generation {selected_gen}')

else:
    if selected_gen == 'All':
        fig = px.scatter(df_gen,
                 x=selected_x,y=selected_y, color='Primary',
                 color_discrete_map=colours, hover_data='Name', size=selected_size)
        fig.update_layout(title=f'{selected_x} vs {selected_y} for {selected_type} Pokemon from all Generations sized by {selected_size}')

    
    elif selected_gen == 'Legendary':
        fig = px.scatter(df_gen[df_gen['Legendary']==True],
                 x=selected_x,y=selected_y, color='Primary',
                 color_discrete_map=colours, hover_data='Name', size=selected_size)
        if selected_type == 'All':
            fig.update_layout(title=f'{selected_x} vs {selected_y} for {selected_type} Legendary Pokemon sized by {selected_size}')
    
        else:
            fig.update_layout(title=f'{selected_x} vs {selected_y} for Legendary {selected_type} Pokemon sized by {selected_size}')

    
    else:
        fig = px.scatter(df_gen[df_gen['Generation']==selected_gen],
                 x=selected_x,y=selected_y, color='Primary',
                 color_discrete_map=colours, hover_data='Name', size=selected_size)
        fig.update_layout(title=f'{selected_x} vs {selected_y} for {selected_type} Pokemon in Generation {selected_gen} sized by {selected_size}')
    
    
#telling streamlit you have a plotly fig to insert
st.plotly_chart(fig)
