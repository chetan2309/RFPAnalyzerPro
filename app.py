import os
from flask import Flask
from markupsafe import Markup
from extensions import db
import markdown

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    db.init_app(app)

    # Add Markdown filter
    @app.template_filter('markdown')
    def markdown_filter(text):
        return Markup(markdown.markdown(text))

    with app.app_context():
        from models import RFP
        from routes import bp
        app.register_blueprint(bp)
        db.create_all()

    return app
