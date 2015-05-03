from models.auth import *


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
    # name = ndb.StringProperty(required=True)
    # profile = ndb.StringProperty(required=True)
    # large_picture = ndb.StringProperty()
    pass