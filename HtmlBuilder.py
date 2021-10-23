import dash
from dash import html
import plotly.graph_objects as go
from dash import dcc
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
            'height':'290px'
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

def buildCpuLoadCell(cpuLoadDisct,pcname):
    df = pd.DataFrame(list(cpuLoadDisct.items()).reverse())
    fig = px.line(df,y=1,x=0,width=300,height=250)
    container = html.Div(
        className="cpuload",
        id="cpuload-"+pcname,
        style={
            'display': 'inline-block',
            'margin-right': '3cm',
            'margin-bottom': '1cm',
            'text-align': 'left',
            'vertical-align': 'top',
            'width':'300px',
            'height':'290px'
        },
        children=[
            html.H5(
                style={"text-align": "left",'margin-bottom': '5px',},
                children="CPU Load"
            ),
            dcc.Graph(id="cpuloadG-"+pcname ,figure=fig,config={
                "displayModeBar":False,
                "displaylogo":False,
                "autosizable": False,
                "fillFrame" : False,
                },
                responsive=False,
            )
        ]
    )
    return container

def buildMemoryCell(memoryDict,pcname):
    container = html.Div(
        className="memory",
        id="memory-"+pcname,
        style={
            'display': 'inline-block',
            'margin-right': '3cm',
            'margin-bottom': '1cm',
            'text-align': 'left',
            'vertical-align': 'top',
        },
        children=[
            html.H5(
                style={"text-align": "left",'margin-bottom': '80px',},
                children="Memory"
            ),
            html.Label(
                id="memory-total-"+pcname,
                children="Total: {}".format(memoryDict['total'])
            ),
            html.Br(),
            html.Label(
                id='memory-available-'+pcname,
                children="Available: {}".format(memoryDict['available'])
            ),
            html.Br(),
            html.Label(
                id='memory-percent-'+pcname,
                children="Percent Usage: {}".format(memoryDict['percentUsage'])
            )
        ]
    )
    return container


def buildNetIoCell(netioDict,pcname):
    container = html.Div(
        className="net",
        id="net-"+pcname,
        style={
            'display': 'inline-block',
            'margin-right': '3cm',
            'margin-bottom': '1cm',
            'text-align': 'left',
            'vertical-align': 'top',
        },
        children=[
            html.H5(
                style={"text-align": "left",'margin-bottom': '80px',},
                children="Network I/O"
            ),
            html.Label(
                id="net-ein-"+pcname,
                children="Error In: {}".format(netioDict['errin'])
            ),
            html.Br(),
            html.Label(
                id='net-eout-'+pcname,
                children="Error Out: {}".format(netioDict['errout'])
            ),
            html.Br(),
            html.Label(
                id='net-din-'+pcname,
                children="Droped In: {}".format(netioDict['dropin'])
            ),
            html.Br(),
            html.Label(
                id="net-dout-"+pcname,
                children="Drop Out: {}".format(netioDict['dropout'])
            ),
            
        ]
    )
    return container


def buildDiskCell(diskDisct,pcname,partition):
    container = html.Div(
        className="disk",
        id="disk-{}-{}".format(partition,pcname),
        style={
            'display': 'inline-block',
            'margin-right': '7cm',
            'margin-bottom': '1cm',
            'text-align': 'left',
            'vertical-align': 'top',
        },
        children=[
            html.H5(
                style={"text-align": "left",'margin-bottom': '80px',},
                children="Partition {}".format(partition)
            ),
            html.Label(
                id="fsys-{}-{}".format(partition,pcname),
                children="File System Type: {}".format(diskDisct['fileSystemType'])
            ),
            html.Br(),
            html.Label(
                id='total-{}-{}'.format(partition,pcname),
                children="Total: {}".format(diskDisct['total'])
            ),
            html.Br(),
            html.Label(
                id='free-{}-{}'.format(partition,pcname),
                children="Free: {}".format(diskDisct['free'])
            ),
            html.Br(),
            html.Label(
                id="used-{}-{}".format(partition,pcname),
                children="Used: {}".format(diskDisct['used'])
            )
        ]
    )
    return container


def buildRow(pcname,cells):
    container = html.Div(
        className="Row",
        id="row-"+pcname,
        style={
            'display': 'inline-block',
            'overflow': 'hidden',
            'white-space': 'nowrap',
            'width':'100%'
        },
        children=[
            buildNodeCell(pcname),
            html.Div(
                className="ScrollableRow",
                id="srow-"+pcname,
                style={
                    'display': 'inline-block',
                    'overflow-x': 'scroll',
                    'white-space': 'nowrap',
                    'width':'100%'
                },
                children=cells
            )
        ]
    )
    return container