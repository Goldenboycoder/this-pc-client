import dash
from dash import html
#import dash_html_components as html
import plotly.graph_objects as go
from dash import dcc
#import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd


def buildNodeCell(pcName):
    container = html.Div(
        className="nodeName", 
        style={
            'display': 'inline-block',
            'vertical-align': 'top',
            'margin-right': '1cm',
            'margin-bottom': '1cm',
            'text-align': 'left',
            ' border-right': '1cm',
            'border-right-style': 'solid',
            'border-right-width': '1px',
            'padding-right': '5mm',
            'height':'320px'
        },
        children=[
            html.H4(children=pcName),
            html.Img(
                src="https://www.freeiconspng.com/uploads/computer-icon--vista-hardware-devices-iconset--icons-land-17.png",
                width=150,
                height=150,
                alt="Computer Icon | Vista Hardware Devices"
            )
        ]
    )

    return container


def buildCpuUtilCell(cpuUtilDict , cpuFreq,pcname):
    """data={}
    for core in cpuUtilDict:
        cpuUtilDict[core] = [cpuUtilDict[core]]"""
    
    df = pd.DataFrame(list(cpuUtilDict.items()))
    fig = px.pie(df,values=1,names=0,width=300,height=250)
    container = html.Div(
        className="cpuUtil",
        id="cpuutil-"+pcname,
        style={
            'display': 'inline-block',
            'margin-right': '3cm',
            'margin-bottom': '1cm',
            'text-align': 'left',
            'vertical-align': 'top',
            'width':'300px',
            'height':'250px'
        },
        children=[
            html.H5(
                style={"text-align": "left",'margin-bottom': '5px',},
                children="CPU Cores Util"
            ),
            dcc.Graph(id="cpuutilG-"+pcname ,figure=fig,config={
                "displayModeBar":False,
                "displaylogo":False,
                "autosizable": False,
                "fillFrame" : False,
                },
                responsive=False,
                ),
            html.Div(
                style={"text-align": "left"},
                children=[
                    html.Label(children="Freq: "),
                    html.Label(id="cpufreq-"+pcname,children=cpuFreq)
                ]
            )
        ]
    )
    return container
