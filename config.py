class Config:
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collo:collins@localhost/blog'
    DEBUG=True
class ProdConfig(Config):
    pass

config_options={
'development':DevConfig,
"production":ProdConfig
}
