class Config:
    SECRET_KEY="collins141"
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collo:collins@localhost/blog'
    DEBUG=True
class ProdConfig(Config):
    pass

config_options={
'development':DevConfig,
"production":ProdConfig
}
