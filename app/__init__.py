from flask import Flask

app = Flask(__name__)

# Import routes only after the app instance is fully initialized
from app.routes import routes  
app.register_blueprint(routes)
