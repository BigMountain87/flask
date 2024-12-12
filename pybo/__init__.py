from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# config.py파일을 읽어옴
import config #DB가 연결 되어 있음

# DB 관련 객체를 생성
db = SQLAlchemy()
migrate = Migrate()

# 서버의 본문
def create_app():
    # 플라스크 서버 객체 생성
    app = Flask(__name__)
    # config 파일을 기반으로 사용
    app.config.from_object(config)

    # ORM -> DB와 연관이 됨
    db.init_app(app)
    migrate.init_app(app, db)
    # models.py 파일을 import 사용
    from . import models

    # 블루프린트 -> 라우터와 관련
    # 주소와 관련한 처리를 모아서 처리
    # main_views : "/" 기준의 페이지를 리턴
    # question_views: "/question/" 하위 주소 관련
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    return app
