from flask import Flask

app = Flask(__name__)

from puppycompany.core.views import core
app.register_blueprint(core)

from puppycompany.error_pages.handlers import error_pages
app.register_blueprint(error_pages)