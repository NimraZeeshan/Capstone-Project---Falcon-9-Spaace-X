# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

launch_sites = spacex_df["Launch Site"].unique()

dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}]
dropdown_options.extend([{'label': site, 'value': site} for site in launch_sites])

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                            'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                html.Label("Select a Launch Site"),

                                dcc.Dropdown(id='site-dropdown',
                                            options=dropdown_options,
                                            value='ALL',
                                            placeholder="Select a Launch Site here",
                                            searchable=True
                                            ),


                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site

                                html.Div(dcc.Graph(id='success-pie-chart')),

                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range

                                dcc.RangeSlider(id='payload-slider',
                                min=0,  # starting point
                                max=10000,  # ending point
                                step=1000,  # interval
                                value=[min_payload, max_payload] ), # current selected range



                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output



@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value')]
)

def get_pie_chart(selected_site):
    # Filter dataframe based on the selected launch site
    if selected_site == 'ALL':
        success_df = spacex_df[spacex_df['class'] == 1].groupby('Launch Site').size().reset_index(name='Success Count')
        # success_df['Success Rate'] = (success_df['Success Count'] / len(spacex_df[spacex_df['class'] == 1])) * 100

        pie_chart = px.pie(
            data_frame=success_df,
            names="Launch Site",
            values='Success Count',
            title="Total Successful Launches for All Sites",
            color_discrete_sequence=px.colors.qualitative.G10,  # Custom color palette
            hole=0.5,  # Size of the hole in the center
            labels={"Launch Site": "Launch Site", "Success Count": "Success Count"},  # Custom labels
        )
        pie_chart.update_layout(
            margin=dict(t=60, b=10, l=10, r=10),  # Adjust margin to provide more space
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=1),  # Position legend
            font=dict(size=12),  # Adjust font size
        )
        return pie_chart
    else:
        # Filter dataframe for successful and unsuccessful launches for the selected site
        filtered_df = spacex_df[(spacex_df['Launch Site'] == selected_site)]
        title = f'Total Successful Launches for {selected_site}'

        # Count the number of successful launches for the selected site
        outcomes_counts = filtered_df.groupby('class').size().reset_index(name='Count')
        outcomes_counts['class'] = outcomes_counts['class'].map({1: 'Success', 0: 'Failure'})

        pie_chart = px.pie(
            data_frame=outcomes_counts,
            names="class",
            values="Count",
            title=title,
            color="class",  # Set color based on outcome
            color_discrete_map={'Success': 'green', 'Failure': 'red'},  # Set custom colors for success and failure
            hole=0.5,  # Size of the hole in the center
            labels={"class": "Outcome", "Count": "Count"},  # Custom labels
        )
        pie_chart.update_layout(
            margin=dict(t=60, b=10, l=10, r=10),  # Adjust margin to provide more space
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),  # Position legend
            font=dict(size=12),  # Adjust font size
        )
        return pie_chart


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output

@app.callback(
    Output('success-payload-scatter-chart', 'figure'),  # Output component ID and property
    [Input('site-dropdown', 'value'),  # Input component IDs and properties
    Input('payload-slider', 'value')]
)


def render_scatter_chart(selected_site, payload_range):
    if selected_site == 'ALL':
        filtered_df = spacex_df
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]



    filtered_df = filtered_df[(filtered_df['Payload Mass (kg)'] >= payload_range[0]) &
                            (filtered_df['Payload Mass (kg)'] <= payload_range[1])]

# Scatter plot for all sites or selected site
    scatter_chart = px.scatter(
        data_frame=filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        color_discrete_sequence=px.colors.qualitative.G10,  # Custom color palette

        size='Payload Mass (kg)',  # Map circle size to payload mass
        s = (50,1000)

        title='Correlation Between Payload and Success for all Sites',
        labels={'class': 'Launch Outcome'},
        hover_name='class'
    )
    scatter_chart.update_layout(
    plot_bgcolor='white',  # Set background color to white
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgrey', zeroline=False, linecolor='black'),  # Set x-axis grid
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgrey', zeroline=False, linecolor='black'),  # Set y-axis grid
    xaxis_showline=True,
    yaxis_showline=True,
    xaxis_linecolor='black',
    yaxis_linecolor='black',
    xaxis_ticks='outside',
    yaxis_ticks='outside',
    xaxis_ticklen=10,
    yaxis_ticklen=10,
    xaxis_tickwidth=2,
    yaxis_tickwidth=2,
    xaxis_tickcolor='black',
    yaxis_tickcolor='black',
    xaxis_title_font=dict(size=14, color='black'),
    yaxis_title_font=dict(size=14, color='black'),
)
    scatter_chart.update_yaxes(tickvals=[0, 1], ticktext=['Failure', 'Success'])

    return scatter_chart

# Run the app
if __name__ == '__main__':
    app.run_server()
