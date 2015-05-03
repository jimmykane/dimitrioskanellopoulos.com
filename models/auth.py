from models.ndb_models import DictModel, NDBCommonModel
from google.appengine.ext import ndb
from oauth2client.appengine import CredentialsProperty


class AuthenticationModel(ndb.Expando, DictModel, NDBCommonModel):
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)


class RunkeeperAuthModel(AuthenticationModel):
    access_token = ndb.StringProperty(required=True)
    access_token_type = ndb.StringProperty(required=True)


class GooglePlusAuthModel(AuthenticationModel):
    credentials = CredentialsProperty(required=True)