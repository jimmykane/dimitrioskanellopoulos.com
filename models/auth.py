import logging
from models.ndb_models import *
from google.appengine.ext import ndb


class AuthenticationModel(ndb.Expando, DictModel, NDBCommonModel):

    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_access_token(cls):
        raise NotImplementedError


class RunkeeperAuthModel(AuthenticationModel):

    #code = ndb.StringProperty()
    token_type = ndb.StringProperty()
    access_token = ndb.StringProperty()