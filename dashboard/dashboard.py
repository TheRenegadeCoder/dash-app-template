import dash

# Global app
app = dash.Dash(
  __name__,
  title="Dashboard Template"
)
server = app.server

if __name__ == '__main__':
  app.run_server(debug=True)
