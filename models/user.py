import logging
from models.ndb_models import *
from google.appengine.ext import ndb

from models.auth import *

class User(ndb.Expando, DictModel, NDBCommonModel):

    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    edit_date = ndb.DateTimeProperty(auto_now=True)