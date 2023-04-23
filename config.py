class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



config = {
    'development': DevelopmentConfig
}
