from flask import Flask

__version__ = '0.1.1'
app = Flask('GithubViewer')

import github_controller


