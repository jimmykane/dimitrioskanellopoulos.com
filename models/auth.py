from models.ndb_models import DictModel, NDBCommonModel
from google.appengine.ext import ndb
from oauth2client.appengine import CredentialsNDBProperty


class AuthenticationModel(ndb.Expando, DictModel, NDBCommonModel):
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)


class RunkeeperAuthModel(AuthenticationModel):
    credentials = CredentialsNDBProperty(required=True)


class GooglePlusAuthModel(AuthenticationModel):
    credentials = CredentialsNDBProperty(required=True)