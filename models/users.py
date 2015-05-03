from models.ndb_models import DictModel, NDBCommonModel
from models.auth import RunkeeperAuthModel, GooglePlusAuthModel
from google.appengine.ext import ndb



class UserModel(ndb.Expando, DictModel, NDBCommonModel):
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)


class RunkeeperUserModel(UserModel, RunkeeperAuthModel):
    runkeeper_user_id = ndb.StringProperty(required=True)


class GooglePlusUserModel(UserModel, GooglePlusAuthModel):
    google_plus_user_id = ndb.StringProperty(required=True)