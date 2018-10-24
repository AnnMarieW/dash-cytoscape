"""
Original Demo: http://js.cytoscape.org/demos/edge-types/
Original Code: https://github.com/cytoscape/cytoscape.js/tree/master/documentation/demos/edge-types

Note: This example is broken because layout takes a function as input:
```
  layout: {
    name: 'grid',
    cols: 4,
    sort: function( a, b ){
      if( a.id() < b.id() ){
        return -1;
      } else if( a.id() > b.id() ){
        return 1;
      } else {
        return 0;
      }
    }
  },
```
"""
import dash_cytoscape
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import json

app = dash.Dash(__name__)
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

with open(f'edge-types/data.json', 'r') as f:
    elements = json.loads(f.read())

with open(f'edge-types/cy-style.json', 'r') as f:
    stylesheet = json.loads(f.read())


# App
app.layout = html.Div([
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        boxSelectionEnabled=False,
        autounselectify=True,
        elements=elements,
        layout={
            'name': 'grid',
            'col': 4
        },
        stylesheet=stylesheet,
        style={
            'width': '100%',
            'height': '100%',
            'position': 'absolute',
            'left': 0,
            'top': 0,
            'z-index': 999
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
