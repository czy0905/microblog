import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	MAIL_SERVER = os.environ.get('MAIL_SERVER')#smtp.qq.com
	MAIL_PORT = os.environ.get('MAIL_PORT')#465
	MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')#重要，QQ邮箱需要使用SSL。True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')#授权码
	ADMINS = ['1517966286@qq.com']

	LANGUAGES =['en', 'zh']

	APPID = os.environ.get('APPID')
	BD_TRANSLATOR_KEY = os.environ.get('BD_TRANSLATOR_KEY')

	ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

	POSTS_PER_PAGE = 3