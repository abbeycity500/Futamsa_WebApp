from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .routes.event import event as event_blueprint
    app.register_blueprint(event_blueprint)
    
    from .routes.news import news as news_blueprint
    app.register_blueprint(news_blueprint)
    
    from .routes.gallery import gallery as gallery_blueprint
    app.register_blueprint(gallery_blueprint)
    
    return app

