import os
class Config:
    SECRET_KEY="collins141"
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    QUOTE_BASE_URL="http://quotes.stormconsultancy.co.uk/random.json"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collo:collins@localhost/blog'
    DEBUG=True
class ProdConfig(Config):
    pass

config_options={
'development':DevConfig,
"production":ProdConfig
}
