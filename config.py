import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'notetaking.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WTF_CSRF_ENABLED = True
SECRET_KEY = 'this-is-not-the-password-you-are-looking-for'
