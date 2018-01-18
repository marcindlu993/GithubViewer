import filters
from GithubViewer import app

# Filters
app.jinja_env.filters['strftime'] = filters._jinja2_filter_datetime


app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)