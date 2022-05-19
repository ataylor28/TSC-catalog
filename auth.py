from collections import UserList
from re import X
from subprocess import call
import tableauserverclient as TSC
import os
import requests
import pandas as pd

class authorize:

    def _token():
        # define environment variables
        TOKEN_NAME = os.environ["TOKEN_NAME"]
        TOKEN_VALUE = os.environ["TOKEN_VALUE"]
        SITENAME = os.environ["SITENAME"]
        SERVER_URL = os.environ["SERVER_URL"]

    def log_in(_token):
        tableau_auth = TSC.PersonalAccessTokenAuth(_token.TOKEN_NAME, _token.TOKEN_VALUE, _token.SITENAME)
        server = TSC.Server(_token.SERVER_URL)
