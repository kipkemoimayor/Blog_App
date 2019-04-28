import os
class Config:
    SECRET_KEY="collins141"
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    QUOTE_BASE_URL="http://quotes.stormconsultancy.co.uk/random.json"

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    '''
    mail config
    '''
    # DEBUG=False
    # BCRYPT_LOG_ROUNDS = 13
    # WTF_CSRF_ENABLED = True
    # DEBUG_TB_ENABLED = False
    # DEBUG_TB_INTERCEPT_REDIRECTS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collo:collins@localhost/blog'
    DEBUG=True
class ProdConfig(Config):
    pass

config_options={
'development':DevConfig,
"production":ProdConfig
}
