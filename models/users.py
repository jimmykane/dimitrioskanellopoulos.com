import logging
from models.ndb_models import *
from google.appengine.ext import ndb

from models.auth import *

class UserModel(ndb.Expando, DictModel, NDBCommonModel):

    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)


class HumanAPIUserModelModel(UserModel, HumanAPIAuthModel):

    email = ndb.StringProperty(required=True)
    human_id = ndb.StringProperty(required=True)


class RunkeeperUserModel(UserModel, RunkeeperAuthModel):

    name = ndb.StringProperty(required=True)
    profile = ndb.StringProperty(required=True)
    large_picture = ndb.StringProperty()

    # Since he was inserted like so
    @property
    def user_id(self):
        return self.key.id()
    pass