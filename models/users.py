from models.ndb_models import DictModel, NDBCommonModel
from models.auth import RunkeeperAuthModel, GooglePlusAuthModel
from google.appengine.ext import ndb



class UserModel(ndb.Expando, DictModel, NDBCommonModel):
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)


class RunkeeperUserModel(UserModel, RunkeeperAuthModel):
    name = ndb.StringProperty(required=True)
    profile = ndb.StringProperty(required=True)
    large_picture = ndb.StringProperty()

    # Since he was inserted like so
    @property
    def user_id(self):
        return self.key.id()


class GooglePlusUserModel(UserModel, GooglePlusAuthModel):
    google_plus_id = ndb.StringProperty(required=True)
    # profile = ndb.StringProperty(required=True)
    # large_picture = ndb.StringProperty()