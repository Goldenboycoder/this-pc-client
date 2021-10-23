import dash
from dash import html
import plotly.graph_objects as go
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import HtmlBuilder as hb
from RedisConnector import RedisClientConnection
from time import sleep
from dash.exceptions import PreventUpdate


app = dash.Dash()
redis = RedisClientConnection("PC-*")

sleep(20) # sleep for redis data to arrive

def init():
    '''
    Get redis data and generate web page on refresh/first load
    '''

    nodesData = redis.getAllNodesData()
    rows=[]
    if nodesData is None:
        return None
    for pc in nodesData:
        partitionsCells=[]
        for part in nodesData[pc]['disks']:
            partitionsCells.append(
                hb.buildDiskCell(nodesData[pc]['disks'][part],pc,part)
            )

        cels = [
            hb.buildCpuUtilCell(nodesData[pc]['cpuUtil'],str(nodesData[pc]['cpuFreq']),pc),
            hb.buildCpuLoadCell(nodesData[pc]['cpuLoad'],pcname=pc),
            hb.buildMemoryCell(nodesData[pc]['memory'],pcname=pc),
            hb.buildNetIoCell(nodesData[pc]['netIO'],pcname=pc)
        ]
        cels.extend(partitionsCells)
        
        row = hb.buildRow(pcname=pc,cells=cels)
        rows.append(row)

    childs = [
        dcc.Interval(
            id='interval-component',
            interval=20*1000, # in milliseconds
            n_intervals=0
        ),
        html.Div(id = 'container', children =rows)
    ]
    return html.Div(id = 'parent', children = childs)

app.layout = init




@app.callback(
    output = Output(component_id='container', component_property= 'children'),
    inputs=Input('interval-component', 'n_intervals')
)
def interval_update(n):
    '''
    Update web page with the new redis data from the buffer.\n
    If no data is found prevent update to web page.
    '''
    rows=[]
    nodesData = redis.getAllNodesData()
    if nodesData is None:
        raise PreventUpdate
    else:
        for pc in nodesData:
            partitionsCells=[]
            for part in nodesData[pc]['disks']:
                partitionsCells.append(
                    hb.buildDiskCell(nodesData[pc]['disks'][part],pc,part)
                )
            cels = [
                hb.buildCpuUtilCell(nodesData[pc]['cpuUtil'],str(nodesData[pc]['cpuFreq']),pc),
                hb.buildCpuLoadCell(nodesData[pc]['cpuLoad'],pcname=pc),
                hb.buildMemoryCell(nodesData[pc]['memory'],pcname=pc),
                hb.buildNetIoCell(nodesData[pc]['netIO'],pcname=pc)
            ]
            cels.extend(partitionsCells)
            
            row = hb.buildRow(pcname=pc,cells=cels)
            rows.append(row)
            
        return rows  



if __name__ == '__main__': 
    app.run_server(debug=True)