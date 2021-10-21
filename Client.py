import dash
from dash import html
#import dash_html_components as html
import plotly.graph_objects as go
from dash import dcc
#import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import HtmlBuilder as hb
import RedisConnector
from time import sleep

app = dash.Dash()
df = px.data.stocks()
redis = RedisConnector("PC-*")

def init():
    sleep(10)
    nodesData = redis.getAllNodesData()
    rows=[]
    
    for pc in nodesData:
        partitionsCells=[]
        for part in nodesData[pc]['disks']:
            partitionsCells.append(
                hb.buildDiskCell(nodesData[pc]['disks'][part],pc,part)
            )

        row = hb.buildRow(pcname=pc,cells=[
            hb.buildCpuUtilCell(nodesData[pc]['cpuUtil'],str(nodesData[pc]['cpuFreq']),pc),
            hb.buildCpuLoadCell(nodesData[pc]['cpuLoad'],pcname=pc),
            hb.buildMemoryCell(nodesData[pc]['memory'],pcname=pc),
            hb.buildNetIoCell(nodesData[pc]['netIO'],pcname=pc)
        ].extend(partitionsCells))
        rows.append(row)

    app.layout = html.Div(id = 'parent', children = [
        dcc.Interval(
            id='interval-component',
            interval=5*1000, # in milliseconds
            n_intervals=0
        )
    ].append(html.Div(id = 'container', children =rows)))


"""
app.layout = html.Div(id = 'parent', children = [
        
        hb.buildRow(pcname="DESKTOP-8GFDG8",cells=[
            hb.buildCpuUtilCell({1:12,2:14,3:2,4:11},str(3.5),"DESKTOP-8GFDG8"),
            hb.buildCpuLoadCell({'min1':4,'min5':10,'min15':20},pcname="DESKTOP-8GFDG8"),
            hb.buildMemoryCell(
                {
                    'total':'16GB',
                    'available':'5GB',
                    'percentUsage':50
                },
                pcname="DESKTOP-8GFDG8"),
            hb.buildNetIoCell(
                {
                    'errin':555,
                    'errout':333,
                    'dropin':222,
                    'dropout':111
                },
                pcname="DESKTOP-8GFDG8"),
            hb.buildDiskCell(
                {
                    'fileSystemType':'NTFS',
                    'total':'1TB',
                    'free':'500GB',
                    'used':'500GB'
                },
                pcname="DESKTOP-8GFDG8",partition='C:\\'
            )
        ])
    ])
"""

def prepUdpate():
    outputs={}


    return outputs



@app.callback(
    output = Output(component_id='container', component_property= 'children'),
    inputs=Input('interval-component', 'n_intervals')
)
def interval_update(n):
    rows=[]
    nodesData = redis.getAllNodesData()
    
    for pc in nodesData:
        partitionsCells=[]
        for part in nodesData[pc]['disks']:
            partitionsCells.append(
                hb.buildDiskCell(nodesData[pc]['disks'][part],pc,part)
            )

        row = hb.buildRow(pcname=pc,cells=[
            hb.buildCpuUtilCell(nodesData[pc]['cpuUtil'],str(nodesData[pc]['cpuFreq']),pc),
            hb.buildCpuLoadCell(nodesData[pc]['cpuLoad'],pcname=pc),
            hb.buildMemoryCell(nodesData[pc]['memory'],pcname=pc),
            hb.buildNetIoCell(nodesData[pc]['netIO'],pcname=pc)
        ].extend(partitionsCells))
        rows.append(row)
        
    return rows  



if __name__ == '__main__': 
    app.run_server()