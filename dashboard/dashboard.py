import dash
from dash import html

# App initialization
app = dash.Dash(
  __name__,
  title="Dashboard Template"
)

# Special line of code for Heroku
server = app.server

# App layout
app.layout = html.Div([
    html.H1("Dashboard Template"),
    html.P(
        """
        Welcome to The Renegade Coder template for Dash apps!
        Place your HTML here to create your own dashboard. 
        Make use of the graphs component of dcc to load Plotly
        graphs. 
        """
    )
])

if __name__ == '__main__':
  app.run_server(debug=True)
