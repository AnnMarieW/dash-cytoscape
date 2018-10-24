"""
Original Demo: http://js.cytoscape.org/demos/concentric-layout/
Original Code: https://github.com/cytoscape/cytoscape.js/blob/master/documentation/demos/concentric-layout/code.js

Note: This example is broken because layout takes a function as input, i.e.
```
  layout: {
    name: 'concentric',
    concentric: function( node ){
      return node.degree();
    },
    levelWidth: function( nodes ){
      return 2;
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

# Load Data
with open(f'concentric-layout/data.json', 'r') as f:
    elements = json.loads(f.read())

# App
app.layout = html.Div([
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        layout={
            'name': 'concentric',
        },
        stylesheet=[{
            'selector': 'node',
            'style': {
                'height': 20,
                'width': 20,
                'background-color': '#30c9bc'
            }
        }, {
            'selector': 'edge',
            'style': {
                'curve-style': 'haystack',
                'haystack-radius': 0,
                'width': 5,
                'opacity': 0.5,
                'line-color': '#a8eae5'
            }
        }],
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
