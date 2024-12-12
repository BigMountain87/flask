from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM -> DB와 연관이 됨
    db.init_app(app)
    migrate.init_app(app, db)
    # models.py 파일을 import 사용
    from . import models

    # 블루프린트 -> 라우트와 관련
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
