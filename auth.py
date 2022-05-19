from collections import UserList
from re import X
from subprocess import call
import tableauserverclient as TSC
import os
import requests
import pandas as pd

def log_in():
    # define environment variables
    TOKEN_NAME = os.environ["TOKEN_NAME"]
    TOKEN_VALUE = os.environ["TOKEN_VALUE"]
    SITENAME = os.environ["SITENAME"]
    SERVER_URL = os.environ["SERVER_URL"]

    tableau_auth = TSC.PersonalAccessTokenAuth(TOKEN_NAME, TOKEN_VALUE, SITENAME)
    server = TSC.Server(SERVER_URL)
    server.auth.sign_in(tableau_auth)
