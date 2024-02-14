import pandas as pd
import plotly as py
from plotly.offline import plot
import plotly.graph_objects as go

#Colour Scheme
COLOUR_YES = '#E69F00' #light orange like ggplot2 orange in R
COLOUR_NO = '#56B4E9' #Light blue like ggplot2 blue in R Colours are supposed to be colour blind friendly


df = pd.read_csv('cleanedData.csv')

df[df['CountyNames'] == 'ROBERTSON'] = df[df['CountyNames'] == 'ROBERTSON'].fillna(0)
# Convert the DataFrame from wide format to long format
df_long = pd.melt(df, id_vars=['CountyNames', 'hasCoalMine'], var_name='Year', value_name='Value')



#give percentage values
df_long['Percentage'] = df_long['Value'].apply(lambda x: f'{x*100:.2f}%')

# Get a list of years
years = df_long['Year'].sort_values().unique()

#Adapted from plotly documentation - https://plotly.com/python/animations/ & Create Racing Bar Graph - Python Plotly (https://www.youtube.com/watch?v=lZNNmaWkiMI) and  https://plotly.com/python/creating-and-updating-figures/#adding-traces
# Create a figure
fig = go.Figure()

# Filter and sort the DataFrame once
df_year = df_long[df_long['Year'] == years[0]].sort_values('Value')
df_top_bottom = pd.concat([df_year.head(10), df_year.tail(10)])

#Trace of data I want to visualise
fig.add_trace(go.Bar(x=df_top_bottom['Value'], 
                     y=df_top_bottom['CountyNames'], 
                     marker_color=df_top_bottom['hasCoalMine'].map({'Yes': COLOUR_YES, 'No': COLOUR_NO}),
                     orientation='h',
                     text=df_top_bottom['Percentage'],  
                     textposition='outside',  # moves the percentage text outside of the bar, was hard to read when inside
                     showlegend=False))  # Hide this trace from the legend

# Trace of the dummy plot to allow for legend
for name, colour in [('County Has Coalmine', COLOUR_YES), ('No Coalmine present', COLOUR_NO)]:
    fig.add_trace(go.Bar(x=[None], 
                         y=[None], 
                    marker_color=colour, 
                    name=name,
                    showlegend=True, 
                    hoverinfo='none',
                    legendgroup=name,
                    hovertemplate=None))


# Creating frames for the animation for each year
# One frame corresponds to one year
fig.frames = [
    go.Frame(
        data=[
            go.Bar(
                x=df_top_bottom['Value'], 
                y=df_top_bottom['CountyNames'], 
                marker_color=df_top_bottom['hasCoalMine'].map({'Yes': COLOUR_YES, 'No': COLOUR_NO}),
                orientation='h',
                text=df_top_bottom['Percentage'], 
                textposition='outside'  # moves the percentage text outside of the bar, was hard to read when inside
            )
        ],
        layout=go.Layout(title_text=f"Kentucky Counties Opioid Transactions per Capita (Top & Bottom 10): {year}"),  # Add a title to the frame {year} updates to show year currently on slider
        name=str(year)  # Set the name of the frame to the year
    ) 
    for year in years 
    #Sort the data for trop and bottom 10
    for df_top_bottom in [pd.concat([df_long[df_long['Year'] == year].sort_values('Value').head(10), df_long[df_long['Year'] == year].sort_values('Value').tail(10)])]
]


# Update layout
fig.update_layout(
    updatemenus=[
        dict(
            type='buttons', 
            showactive=False,
            buttons=[
                dict(label='Play &#9658;', method='animate', args=[None,{"frame": {"duration": 2000, "redraw": True}, "transition": {"duration": 2000}} ]),
                dict(label='Pause \u23F8', method='animate', args=[[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}]),
              
            ],
            pad={"r": 100, "t": 70}, # I added padding as buttons were covering the county labels 
        )
    ],
    sliders=[
        dict(
            active=0, 
            steps=[dict(label=str(year), method='animate', args=[[str(year)]]) for year in years]  # Use the string version of the year
        
        )
    ],
    plot_bgcolor='white',
    xaxis=dict(showticklabels=False, range=[0,1]),  # Hide x-axis tick labels

)


plot(fig)
