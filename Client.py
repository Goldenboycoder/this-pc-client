import dash
from dash import html
#import dash_html_components as html
import plotly.graph_objects as go
from dash import dcc
#import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import HtmlBuilder as hb

app = dash.Dash()
df = px.data.stocks()

app.layout = html.Div(id = 'parent', children = [
    
    hb.buildRow(pcname="DESKTOP-8GFDG8",cells=[
        hb.buildCpuUtilCell({1:12,2:14,3:2,4:11},str(3.5),"DESKTOP-8GFDG8"),
        hb.buildCpuLoadCell({'min1':4,'min5':10,'min15':20},pcname="DESKTOP-8GFDG8")
    ])
])

@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x = df['date'], y = df['{}'.format(dropdown_value)],\
                     line = dict(color = 'firebrick', width = 4))
                     ])
    
    fig.update_layout(title = 'Stock prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  



if __name__ == '__main__': 
    app.run_server()