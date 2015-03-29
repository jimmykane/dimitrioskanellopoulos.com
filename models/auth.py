import logging
from models.ndb_models import *
from google.appengine.ext import ndb


class AuthenticationModel(ndb.Expando, DictModel, NDBCommonModel):

    access_token = ndb.StringProperty(required=True)
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)

class HumanAPIAuthModel(AuthenticationModel):

    access_token_key = ndb.StringProperty(required=True)
    public_token = ndb.StringProperty(required=True)