from os import path


BASE_DIR = path.dirname(path.dirname(__file__))

engine = 'sqlite:///'
engine += path.join(path.dirname(BASE_DIR), 'test.db')
s = 'fwJP6wU9dQXKMWAfSbDW46VyU7SbSXH3xLYMEsw4mdrtrRGE'
s += 'DRfqS7VAzwcWnRuQ69JNT9GsNxQdcQsuTmXZyMexUNMDXvck'


class Config():
    SECRET_KEY = s
    SQLALCHEMY_DATABASE_URI = engine
    SQLALCHEMY_TRACK_MODIFICATIONS = True
