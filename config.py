import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsimagesstore'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '5w48uE05iLRoW3maHuKdfPl8UW1fDT5O/XlZ47CiwSE+kSQJzKPTIKb55gp9/8Zli3n8mVNgOqv17CWb+jpaqA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sqlserver-west.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'sqldb-west'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'sql@dminPass'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # CLIENT_SECRET = "6b.aNYPh0T8DY79Pm22y3_O.t_YfPU_4VB"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    # CLIENT_ID = "5628a6bd-095e-47e5-a371-320791da9f14"
    CLIENT_ID = os.getenv("CLIENT_ID")
    if not CLIENT_ID:
        raise ValueError("Need to define CLIENT_ID environment variable")

    REDIRECT_PATH = "/.auth/login/aad/callback"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session