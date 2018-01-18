import dateutil
from dateutil import parser
from flask import Flask

import extension_fun

app = Flask(__name__)


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format = extension_fun.set_format(fmt)
    return native.strftime(format)

