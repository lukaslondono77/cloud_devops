from flask import Flask

app = Flask(__name__)

# Import and register Blueprint
from app.routes import routes
app.register_blueprint(routes, url_prefix='/')
