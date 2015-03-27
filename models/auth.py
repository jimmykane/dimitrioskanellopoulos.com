import logging
from models.ndb_models import *
from google.appengine.ext import ndb


class AuthenticationModel(ndb.Expando, DictModel, NDBCommonModel):

    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)

class HumanAPIAuthModel(AuthenticationModel):

    token_type = ndb.StringProperty()
    access_token = ndb.StringProperty()