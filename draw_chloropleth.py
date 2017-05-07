import plotly as py
import pandas as pd

py.tools.set_credentials_file(username='aditya311091', api_key='nLXCFNDDKFf3LhcES36p')

def draw_chloropleth(output):
    """
    Make a US map chloropleth map of state-level accumulations
    
    Input: output, type = Pandas Dataframe consisting of final output of main.py
    
    Output: Inline plot of US state-level accumulations
    """

    scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
                [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = output['Code'],
            z = output['Insured Limit ($ in thousands)'].astype(float),
            locationmode = 'USA-states',
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                ) ),
            colorbar = dict(
                title = "Millions USD")
            ) ]

    layout = dict(
            title = 'State-Level Accumulations by Underwriter Sheila',
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
                 )

    fig = dict( data=data, layout=layout )
    py.plotly.iplot( fig, filename='d3-cloropleth-map' )