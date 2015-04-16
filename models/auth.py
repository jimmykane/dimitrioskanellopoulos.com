import logging
from models.ndb_models import *
from google.appengine.ext import ndb


class AuthenticationModel(ndb.Expando, DictModel, NDBCommonModel):

    access_token = ndb.StringProperty(required=True)
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)


class RunkeeperAuthModel(AuthenticationModel):

    access_token = ndb.StringProperty(required=True)
    access_token_type = ndb.StringProperty(required=True)