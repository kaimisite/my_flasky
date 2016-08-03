from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from config import config

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()


def create_app(config_name):
    '''工厂函数'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 导入配置类
    config[config_name].init_app(app)  # 初始化程序实例

    bootstrap.init_app(app)  # 初始化扩展
    moment.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint)

    return app


