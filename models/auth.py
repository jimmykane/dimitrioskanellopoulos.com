import logging
from models.ndb_models import *
from google.appengine.ext import ndb



class CodeAuth(ndb.Expando, DictModel, NDBCommonModel):

    # title = ndb.StringProperty()
    # duration = ndb.IntegerProperty()
    # queued_by_person_key = ndb.KeyProperty()
    # play_count = ndb.IntegerProperty(required=True, default=0)
    #
    #
    # creation_date = ndb.DateTimeProperty(auto_now_add=True)
    # edit_date = ndb.DateTimeProperty(auto_now=True)
    # available = ndb.BooleanProperty(default=True)
    pass

class RunkeeperAuth(CodeAuth):

    code = ndb.StringProperty()
    token_type = ndb.StringProperty()
    access_token = ndb.StringProperty()
    pass